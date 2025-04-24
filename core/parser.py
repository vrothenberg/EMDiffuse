"""
Configuration Parser Module for EMDiffuse

This module provides utilities for parsing configuration files, initializing objects,
and managing file paths for the EMDiffuse project. It serves as a central configuration
management system that allows for flexible model and dataset configuration.

Author: EMDiffuse Team
Date: April 2025
License: See LICENSE file
"""

import os
from collections import OrderedDict
import json
from pathlib import Path
from datetime import datetime
from functools import partial
import importlib
from types import FunctionType
import shutil


def init_obj(opt, logger, *args, default_file_name='default file', given_module=None, init_type='Network',
             **modify_kwargs):
    """
    Finds a function or class with the name given in the config and returns an initialized instance.
    
    This function dynamically imports and initializes objects (classes or functions) based on
    configuration options. It's a key part of the factory pattern used throughout EMDiffuse.
    
    Args:
        opt (dict or str): Configuration options containing the name and arguments for initialization.
            If a string is provided, it's converted to a dict with the string as the 'name' key.
        logger (InfoLogger): Logger instance for logging initialization information.
        *args: Additional positional arguments to pass to the initialized object.
        default_file_name (str): Default module name to import from if not specified in opt.
        given_module (module, optional): Pre-imported module to use instead of importing.
        init_type (str): Type of object being initialized (for logging purposes).
        **modify_kwargs: Additional keyword arguments to override or add to those in opt.
    
    Returns:
        object: Initialized instance of the specified class or partial function.
    """
    if opt is None or len(opt) < 1:
        logger.info('Option is None when initialize {}'.format(init_type))
        return None

    ''' default format is dict with name key '''
    if isinstance(opt, str):
        opt = {'name': opt}
        logger.warning('Config is a str, converts to a dict {}'.format(opt))

    name = opt['name']
    ''' name can be list, indicates the file and class name of function '''
    if isinstance(name, list):
        file_name, class_name = name[0], name[1]
    else:
        file_name, class_name = default_file_name, name

    if given_module is not None:
        module = given_module
    else:
        module = importlib.import_module(file_name)

    attr = getattr(module, class_name)
    kwargs = opt.get('args', {})
    kwargs.update(modify_kwargs)
    ''' import class or function with args '''
    if isinstance(attr, type):
        ret = attr(*args, **kwargs)
        ret.__name__ = ret.__class__.__name__
    elif isinstance(attr, FunctionType):
        ret = partial(attr, *args, **kwargs)
        ret.__name__ = attr.__name__
        # ret = attr
    logger.info('{} [{:s}() form {:s}] is created.'.format(init_type, class_name, file_name))

    return ret


def mkdirs(paths):
    """
    Create directories for the given paths.
    
    Args:
        paths (str or list): Path or list of paths to create.
    """
    if isinstance(paths, str):
        os.makedirs(paths, exist_ok=True)
    else:
        for path in paths:
            os.makedirs(path, exist_ok=True)


def get_timestamp():
    """
    Get the current timestamp in a formatted string.
    
    Returns:
        str: Formatted timestamp string (YYmmdd_HHMMSS).
    """
    return datetime.now().strftime('%y%m%d_%H%M%S')


def write_json(content, fname):
    """
    Write content to a JSON file.
    
    Args:
        content (dict): Content to write to the JSON file.
        fname (str): Path to the output JSON file.
    """
    fname = Path(fname)
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)


class NoneDict(dict):
    """
    A dictionary subclass that returns None for missing keys instead of raising KeyError.
    """
    def __missing__(self, key):
        return None


def dict_to_nonedict(opt):
    """
    Convert a nested dictionary to NoneDict, which returns None for missing keys.
    
    Args:
        opt (dict, list, or other): The input to convert. If dict, converts to NoneDict.
            If list, processes each element. Otherwise, returns as is.
    
    Returns:
        NoneDict, list, or other: The converted structure.
    """
    if isinstance(opt, dict):
        new_opt = dict()
        for key, sub_opt in opt.items():
            new_opt[key] = dict_to_nonedict(sub_opt)
        return NoneDict(**new_opt)
    elif isinstance(opt, list):
        return [dict_to_nonedict(sub_opt) for sub_opt in opt]
    else:
        return opt


def dict2str(opt, indent_l=1):
    """
    Convert a nested dictionary to a formatted string for logging.
    
    Args:
        opt (dict): The dictionary to convert.
        indent_l (int): The indentation level to start with.
    
    Returns:
        str: A formatted string representation of the dictionary.
    """
    msg = ''
    for k, v in opt.items():
        if isinstance(v, dict):
            msg += ' ' * (indent_l * 2) + k + ':[\n'
            msg += dict2str(v, indent_l + 1)
            msg += ' ' * (indent_l * 2) + ']\n'
        else:
            msg += ' ' * (indent_l * 2) + k + ': ' + str(v) + '\n'
    return msg


def parse(args):
    """
    Parse configuration from a JSON file and command-line arguments.
    
    This function reads a JSON configuration file, processes it to remove comments,
    and updates it with command-line arguments. It also sets up directories for
    experiment results and code backup.
    
    Args:
        args (argparse.Namespace): Command-line arguments.
    
    Returns:
        NoneDict: A dictionary-like object containing the configuration with None for missing keys.
    """
    # Read and parse the JSON configuration file
    json_str = ''
    with open(args.config, 'r') as f:
        for line in f:
            line = line.split('//')[0] + '\n'  # Remove comments
            json_str += line
    opt = json.loads(json_str, object_pairs_hook=OrderedDict)

    ''' replace the config context using args '''
    opt['phase'] = args.phase
    if args.gpu is not None:
        opt['gpu_ids'] = [int(id) for id in args.gpu.split(',')]
    if args.batch is not None:
        opt['datasets'][opt['phase']]['dataloader']['args']['batch_size'] = args.batch
    if args.path is not None:
        opt['datasets'][opt['phase']]['which_dataset']['args']['data_root'] = args.path
    if args.z_times is not None:
        opt['datasets'][opt['phase']]['which_dataset']['args']['z_times'] = args.z_times
    if args.lr is not None:
        opt['model']['which_model']['args']['optimizers'][0]['lr'] = args.lr
    if args.step is not None:
        opt['model']['which_networks'][0]['args']['beta_schedule'][opt['phase']]['n_timestep'] = args.step
    ''' set cuda environment '''
    if len(opt['gpu_ids']) > 1:
        opt['distributed'] = True
    else:
        opt['distributed'] = False

    ''' update name '''
    if args.debug:
        opt['name'] = 'debug_{}'.format(opt['name'])
    elif opt['finetune_norm']:
        opt['name'] = 'finetune_{}'.format(opt['name'])
    else:
        opt['name'] = '{}_{}'.format(opt['phase'], opt['name'])

    ''' set log directory '''
    experiments_root = os.path.join(opt['path']['base_dir'], '{}_{}'.format(opt['name'], get_timestamp()))
    mkdirs(experiments_root)
    print('results and model will be saved in {}'.format(experiments_root))
    ''' save json '''
    write_json(opt, '{}/config.json'.format(experiments_root))

    ''' change folder relative hierarchy '''
    opt['path']['experiments_root'] = experiments_root
    for key, path in opt['path'].items():
        if 'resume' not in key and 'base' not in key and 'root' not in key:
            opt['path'][key] = os.path.join(experiments_root, path)
            mkdirs(opt['path'][key])
    if args.resume is not None:
        opt['path']['resume_state'] = args.resume

    ''' debug mode '''
    if 'debug' in opt['name']:
        opt['train'].update(opt['debug'])

    ''' code backup '''
    for name in os.listdir('.'):
        if name in ['config', 'models', 'core', 'slurm', 'data']:
            dst = os.path.join(opt['path']['code'], name)
            if os.path.exists(dst):
                shutil.rmtree(dst)
                shutil.copytree(name, dst)
            # shutil.copytree(name,dst , ignore=shutil.ignore_patterns("*.pyc", "__pycache__"))
        if '.py' in name or '.sh' in name:
            shutil.copy(name, opt['path']['code'])
    opt['mean'] = args.mean
    return dict_to_nonedict(opt)
