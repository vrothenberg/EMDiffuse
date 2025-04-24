# Configuration Files

This directory contains JSON configuration files for the different variants of the EMDiffuse model. These files define the model architecture, training parameters, and dataset settings.

## Files and Functionality

### EMDiffuse-n.json
- **Purpose**: Configuration for the EMDiffuse-n model for EM denoising.
- **Key Components**:
  - Model architecture parameters for the denoising task.
  - Training and testing settings.
  - Dataset and dataloader configurations.

### EMDiffuse-n-big.json
- **Purpose**: Configuration for a larger version of the EMDiffuse-n model.
- **Key Components**:
  - Similar to EMDiffuse-n.json but with a larger model architecture.

### EMDiffuse-n-transfer.json
- **Purpose**: Configuration for transfer learning with the EMDiffuse-n model.
- **Key Components**:
  - Settings for fine-tuning a pre-trained EMDiffuse-n model on new data.

### EMDiffuse-r.json
- **Purpose**: Configuration for the EMDiffuse-r model for EM super-resolution.
- **Key Components**:
  - Model architecture parameters for the super-resolution task.
  - Training and testing settings.
  - Dataset and dataloader configurations.

### vEMDiffuse-i.json
- **Purpose**: Configuration for the vEMDiffuse-i model for isotropic reconstruction with isotropic training data.
- **Key Components**:
  - 3D model architecture parameters.
  - Settings for training and testing on isotropic data.
  - Dataset and dataloader configurations for 3D volumes.

### vEMDiffuse-a.json
- **Purpose**: Configuration for the vEMDiffuse-a model for isotropic reconstruction without isotropic training data.
- **Key Components**:
  - 3D model architecture parameters.
  - Settings for training and testing on anisotropic data.
  - Dataset and dataloader configurations for 3D volumes.

## Configuration Structure

The configuration files follow a common structure:

### General Settings
- `name`: Name of the experiment.
- `norm`: Whether to normalize the data.
- `gpu_ids`: List of GPU IDs to use.
- `seed`: Random seed for reproducibility.
- `task`: Task type (denoise, super-res, etc.).

### Path Settings
- `path`: Dictionary of file paths for logs, checkpoints, results, etc.

### Dataset Settings
- `datasets`: Dictionary of dataset configurations for training and testing.
  - `which_dataset`: Dataset class and arguments.
  - `dataloader`: Dataloader arguments and validation split.

### Model Settings
- `model`: Dictionary of model configurations.
  - `which_model`: Model class and arguments.
  - `which_networks`: List of network configurations.
  - `which_losses`: List of loss functions.
  - `which_metrics`: List of evaluation metrics.

### Training Settings
- `train`: Dictionary of training parameters.
  - `n_epoch`: Maximum number of epochs.
  - `n_iter`: Maximum number of iterations.
  - `val_epoch`: Validation frequency.
  - `save_checkpoint_epoch`: Checkpoint saving frequency.
  - `log_iter`: Logging frequency.
  - `tensorboard`: Whether to enable TensorBoard logging.

### Debug Settings
- `debug`: Dictionary of debug parameters that override training parameters.

## Usage

The configuration files are used by the `run.py` script to set up the model, dataset, and training/testing parameters. The configuration file is specified using the `-c` or `--config` argument:

```bash
python run.py -c config/EMDiffuse-n.json -b 16 --gpu 0,1,2,3 --port 20022 --path /path/to/data --lr 5e-5
```

Command-line arguments can override specific configuration parameters, such as batch size (`-b`), GPU IDs (`--gpu`), data path (`--path`), and learning rate (`--lr`).
