"""
Configuration Class for EMDiffuse

This module provides a configuration class for the EMDiffuse project that encapsulates
all the command-line arguments and configuration options. It serves as a convenient
way to pass configuration parameters throughout the codebase.

Author: EMDiffuse Team
Date: April 2025
License: See LICENSE file
"""


class EMDiffuseConfig:
    """
    Configuration class for EMDiffuse that stores all command-line arguments and settings.
    
    This class provides a convenient way to access configuration parameters throughout
    the codebase. It implements custom attribute access methods to provide a flexible
    interface for accessing configuration options.
    
    Attributes:
        path (str): Path to the data directory.
        config (str): Path to the configuration file.
        phase (str): Phase of operation ('train' or 'test').
        batch (int): Batch size for training or inference.
        gpu (str): GPU IDs to use (comma-separated string).
        debug (bool): Whether to run in debug mode.
        z_times (int, optional): Subsampling factor for 3D volumes.
        port (str): Port for distributed training.
        resume (str, optional): Path to resume training from a checkpoint.
        mean (int): Number of samples to generate and average.
        lr (float): Learning rate for training.
        step (int, optional): Number of diffusion steps.
    """

    def __init__(self, config, path, phase, batch_size, lr=5e-5, resume=None, 
                 gpu='0', subsample=None, port='21012', mean=2, step=None):
        """
        Initialize the EMDiffuseConfig with the given parameters.
        
        Args:
            config (str): Path to the configuration file.
            path (str): Path to the data directory.
            phase (str): Phase of operation ('train' or 'test').
            batch_size (int): Batch size for training or inference.
            lr (float, optional): Learning rate for training. Defaults to 5e-5.
            resume (str, optional): Path to resume training from a checkpoint. Defaults to None.
            gpu (str, optional): GPU IDs to use (comma-separated string). Defaults to '0'.
            subsample (int, optional): Subsampling factor for 3D volumes. Defaults to None.
            port (str, optional): Port for distributed training. Defaults to '21012'.
            mean (int, optional): Number of samples to generate and average. Defaults to 2.
            step (int, optional): Number of diffusion steps. Defaults to None.
        """
        self.path = path
        self.config = config
        self.phase = phase
        self.batch = batch_size
        self.gpu = gpu
        self.debug = False
        self.z_times = subsample
        self.port = port
        self.resume = resume
        self.mean = mean
        self.lr = lr
        self.step = step

    def __getattr__(self, item):
        """
        Custom attribute access method that returns None for missing attributes.
        
        This method is called when an attribute access is attempted but the attribute
        doesn't exist in the instance's __dict__.
        
        Args:
            item (str): The name of the attribute being accessed.
            
        Returns:
            Any: The value of the attribute if it exists, None otherwise.
        """
        try:
            return self.__dict__[item]
        except KeyError:
            return None

    def __setattr__(self, key, value):
        """
        Custom attribute setting method.
        
        Args:
            key (str): The name of the attribute to set.
            value (Any): The value to set the attribute to.
        """
        self.__dict__[key] = value

    def __contains__(self, item):
        """
        Enable the use of 'in' operator to check for attribute existence.
        
        Args:
            item (str): The name of the attribute to check for.
            
        Returns:
            bool: True if the attribute exists, False otherwise.
        """
        return item in self.__dict__
