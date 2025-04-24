# Data Module

The Data module provides functionality for loading and processing data for the EMDiffuse project. It includes dataset classes for different types of data and utility functions for data augmentation and processing.

## Files and Functionality

### __init__.py
- **Purpose**: Provides functions for creating and initializing dataloaders and datasets.
- **Key Components**:
  - `define_dataloader`: Function to create train/test dataloader and validation dataloader.
  - `define_dataset`: Function to create dataset instances based on configuration.
  - `subset_split`: Function to split a dataset into non-overlapping subsets.

### dataset.py
- **Purpose**: Implements dataset classes for different types of data.
- **Key Components**:
  - `EMDiffusenDataset`: Dataset class for 2D image denoising and super-resolution.
  - `vEMDiffuseTrainingDatasetPatches`: Dataset class for vEMDiffuse training using downloaded subvolumes.
  - `vEMDiffuseTrainingDatasetVolume`: Dataset class for vEMDiffuse training using whole isotropic volumes.
  - `vEMDiffuseTestIsotropic`: Dataset class for testing vEMDiffuse-i on isotropic volumes.
  - `vEMDiffuseTestAnIsotropic`: Dataset class for testing vEMDiffuse-i on anisotropic volumes.
  - Utility functions for finding maximum numbers in folders and loading images.

## Utility Functions

The `util` directory contains utility functions for data augmentation and processing:

### auto_augment.py
- **Purpose**: Provides functions for automatic data augmentation.
- **Key Components**:
  - Functions for applying various augmentations to images.

### mask.py
- **Purpose**: Provides functions for creating and applying masks to images.
- **Key Components**:
  - Functions for generating and applying masks for training and inference.

## Dataset Classes

### EMDiffusenDataset
- **Purpose**: Dataset class for 2D image denoising and super-resolution.
- **Key Features**:
  - Loads paired noisy/clean or low-res/high-res images.
  - Applies data augmentation during training.
  - Returns a dictionary with 'gt_image', 'cond_image', and 'path'.

### vEMDiffuseTrainingDatasetPatches
- **Purpose**: Dataset class for vEMDiffuse training using downloaded subvolumes.
- **Key Features**:
  - Loads 3D volume data from patches.
  - Selects slices based on the z_times parameter.
  - Applies data augmentation during training.
  - Returns a dictionary with 'gt_image', 'cond_image', and 'path'.

### vEMDiffuseTrainingDatasetVolume
- **Purpose**: Dataset class for vEMDiffuse training using whole isotropic volumes.
- **Key Features**:
  - Loads 3D volume data from a whole volume.
  - Randomly selects patches from the volume.
  - Applies data augmentation during training.
  - Returns a dictionary with 'gt_image', 'cond_image', and 'path'.

### vEMDiffuseTestIsotropic
- **Purpose**: Dataset class for testing vEMDiffuse-i on isotropic volumes.
- **Key Features**:
  - Loads isotropic volume data.
  - Downsamples the volume for testing.
  - Returns a dictionary with 'gt_image', 'cond_image', and 'path'.

### vEMDiffuseTestAnIsotropic
- **Purpose**: Dataset class for testing vEMDiffuse-i on anisotropic volumes.
- **Key Features**:
  - Loads anisotropic volume data.
  - Returns a dictionary with 'gt_image', 'cond_image', and 'path'.

## Data Augmentation

The dataset classes apply various data augmentation techniques during training:

- **Flipping**: Random horizontal flipping of images.
- **Rotation**: Random 90-degree rotation of images.
- **Gaussian Blur**: Random application of Gaussian blur to input images.

## Usage

The data module is used to create dataloaders for training and testing the diffusion models. The main entry points are:

- `define_dataloader`: Used to create dataloaders based on configuration.
- `define_dataset`: Used to create dataset instances based on configuration.

The dataset classes are instantiated through the `init_obj` function in the core module, based on the configuration provided in the JSON configuration files.
