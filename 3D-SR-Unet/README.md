# 3D-SR-Unet

This directory contains an implementation of a 3D Super-Resolution U-Net (SRUNet) for enhancing the resolution of 3D electron microscopy volumes, particularly along the z-axis.

## Files and Functionality

### main.py
- **Purpose**: Main entry point for training the 3D-SR-Unet model.
- **Key Components**:
  - `train_distributed`: Function for distributed training across multiple GPUs.
  - `subset_split`: Function for splitting datasets into training and validation sets.
  - Command-line argument parsing for training parameters.

### model.py
- **Purpose**: Implements the 3D-SR-Unet architecture and loss function.
- **Key Components**:
  - `SRUNet`: Class implementing the 3D Super-Resolution U-Net architecture.
  - `CubicWeightedPSNRLoss`: Custom loss function for super-resolution training.
  - Helper functions for creating 3D convolutional layers.

### data.py
- **Purpose**: Implements dataset classes for loading and processing 3D volume data.
- **Key Components**:
  - `KidneySRUData`: Dataset class for loading kidney data for super-resolution training.

### train.py
- **Purpose**: Implements the training loop for the 3D-SR-Unet model.
- **Key Components**:
  - `train_cnn`: Function for training the CNN model with validation.

## Architecture

The 3D-SR-Unet architecture is a 3D U-Net designed specifically for super-resolution tasks. It consists of:

1. **Encoder Path**:
   - Three convolutional blocks with max pooling between them.
   - Each block contains multiple 3D convolutional layers with ReLU activation.

2. **Decoder Path**:
   - Transposed convolutions (fracconv) for upsampling.
   - Skip connections from the encoder path.
   - Convolutional blocks for feature processing.

3. **Output Layer**:
   - Final convolutional layer to produce the super-resolved output.

The model is designed to upsample the input volume by a factor of `up_scale` (default is 6) along the z-axis, which is particularly useful for enhancing the resolution of anisotropic electron microscopy volumes.

## Loss Function

The `CubicWeightedPSNRLoss` is a custom loss function designed for super-resolution tasks. It:

1. Computes the error between the upsampled input and the target.
2. Uses this error to create a weight map that emphasizes areas with high error.
3. Applies this weight map to the MSE loss between the prediction and the target.

This weighted approach helps the model focus on areas that are difficult to reconstruct, improving the overall quality of the super-resolved output.

## Usage

The model can be trained using the `main.py` script with various command-line arguments:

```bash
python main.py --b 16 --epoch 100 --lr 1e-4 --output ./model_output --gpus 0,1,2,3
```

Key arguments include:
- `--b`: Batch size
- `--epoch`: Number of training epochs
- `--lr`: Learning rate
- `--output`: Output directory for saving models
- `--gpus`: GPU indices for training
- `--seed`: Random seed for reproducibility
- `--num_worker`: Number of data loading workers

## Integration with EMDiffuse

The 3D-SR-Unet serves as an alternative approach to the vEMDiffuse models for isotropic reconstruction of electron microscopy volumes. While vEMDiffuse uses diffusion models, 3D-SR-Unet uses a more traditional U-Net architecture specifically designed for super-resolution along the z-axis.
