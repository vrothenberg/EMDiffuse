# RAFT Core Module

This directory contains the core implementation of RAFT (Recurrent All Pairs Field Transforms) for optical flow, which is used in the EMDiffuse project for image registration and alignment.

## Files and Functionality

### raft.py
- **Purpose**: Implements the RAFT model for optical flow estimation.
- **Key Components**:
  - `RAFT`: Class implementing the RAFT architecture.
  - Functions for feature extraction, correlation, and flow estimation.

### register.py
- **Purpose**: Implements image registration for the EMDiffuse-n denoising task.
- **Key Components**:
  - `registration`: Main function for registering and aligning images.
  - `process_pair`: Function for processing pairs of images (noisy and clean).
  - Helper functions for image warping, flow computation, and visualization.

### register_custom.py
- **Purpose**: Implements custom image registration for user-provided datasets.
- **Key Components**:
  - Similar to register.py but adapted for custom dataset formats.

### super_res_register.py
- **Purpose**: Implements image registration for the EMDiffuse-r super-resolution task.
- **Key Components**:
  - Similar to register.py but adapted for super-resolution datasets.

### align_functions.py
- **Purpose**: Provides functions for image alignment.
- **Key Components**:
  - `align_images`: Function for aligning images using feature matching.
  - `mkdir`: Helper function for creating directories.
  - Other utility functions for image alignment.

### corr.py
- **Purpose**: Implements correlation volume computation for optical flow.
- **Key Components**:
  - `CorrBlock`: Class for computing correlation volumes.
  - Functions for correlation lookup and processing.

### update.py
- **Purpose**: Implements the update operator for the RAFT model.
- **Key Components**:
  - `FlowHead`: Class for predicting flow from features.
  - `ConvGRU`: Class implementing a convolutional GRU for recurrent processing.
  - `SepConvGRU`: Class implementing a separable convolutional GRU.

### extractor.py
- **Purpose**: Implements feature extractors for the RAFT model.
- **Key Components**:
  - `BasicEncoder`: Class implementing a basic feature encoder.
  - `SmallEncoder`: Class implementing a smaller feature encoder.

### datasets.py
- **Purpose**: Implements dataset classes for training and evaluating RAFT.
- **Key Components**:
  - Dataset classes for various optical flow datasets.
  - Data augmentation and preprocessing functions.

### raftConfig.py
- **Purpose**: Provides configuration parameters for the RAFT model.
- **Key Components**:
  - Configuration parameters for model architecture and training.

## Usage in EMDiffuse

In the EMDiffuse project, RAFT is used for:

1. **Image Registration**: Aligning noisy/low-resolution images with their clean/high-resolution counterparts.
2. **Patch Extraction**: Extracting aligned patches from image pairs for training.
3. **Flow Estimation**: Computing optical flow between images for warping and alignment.

The main entry points for using RAFT in EMDiffuse are:

- `register.py`: For registering and aligning images for the denoising task.
- `register_custom.py`: For registering and aligning custom datasets.
- `super_res_register.py`: For registering and aligning images for the super-resolution task.

These scripts are called from the main EMDiffuse scripts to prepare data for training and testing.

## Example Usage

```bash
python register.py --path /data/EMDiffuse_dataset/brain_train --tissue Brain --patch_size 256 --overlap 0.125
```

This command will:
1. Load the RAFT model.
2. Process the brain dataset at the specified path.
3. Register and align the noisy and clean images.
4. Extract patches of size 256x256 with an overlap of 12.5%.
5. Save the aligned patches for training.

## Integration with EMDiffuse

The RAFT module is integrated with EMDiffuse through the data preparation pipeline. Before training the diffusion models, the raw data is processed using RAFT to ensure proper alignment between input and target images, which is crucial for supervised learning tasks like denoising and super-resolution.
