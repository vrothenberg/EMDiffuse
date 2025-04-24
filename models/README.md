# Models Module

The Models module contains the implementation of the diffusion models used in the EMDiffuse project. It includes model definitions, network architectures, loss functions, and evaluation metrics.

## Files and Functionality

### __init__.py
- **Purpose**: Provides functions for creating and initializing models, networks, losses, and metrics.
- **Key Components**:
  - `create_model`: Function to create a model instance based on configuration.
  - `define_network`: Function to define and initialize a network.
  - `define_loss`: Function to define a loss function.
  - `define_metric`: Function to define an evaluation metric.
  - `create_EMDiffuse`: Function to create an EMDiffuse model with all components.

### EMDiffuse_model.py
- **Purpose**: Implements the EMDiffuse model for 2D image enhancement (denoising and super-resolution).
- **Key Components**:
  - `DiReP`: Class that implements the diffusion-based restoration pipeline.
  - `EMA`: Class for Exponential Moving Average of model weights.

### EMDiffuse_network.py
- **Purpose**: Implements the network architecture for the EMDiffuse model.
- **Key Components**:
  - `Network`: Class that implements the diffusion network.
  - Functions for the forward and reverse diffusion processes.
  - Beta schedule functions for controlling the noise addition process.

### vEMDiffuse_model.py
- **Purpose**: Implements the vEMDiffuse model for 3D volume enhancement (isotropic reconstruction).
- **Key Components**:
  - `DiReP`: Class that implements the diffusion-based restoration pipeline for volumes.
  - `EMA`: Class for Exponential Moving Average of model weights.

### vEMDiffuse_network.py
- **Purpose**: Implements the network architecture for the vEMDiffuse model.
- **Key Components**:
  - `Network`: Class that implements the 3D diffusion network.
  - Functions for the forward and reverse diffusion processes.
  - Beta schedule functions for controlling the noise addition process.

### loss.py
- **Purpose**: Implements loss functions for training the models.
- **Key Components**:
  - `mse_loss`: Mean Squared Error loss function.
  - `l1_loss`: L1 loss function.
  - `mse_var_loss`: MSE loss with variance weighting for uncertainty estimation.
  - `pin_loss`: Pinball loss for quantile regression.
  - `PinballLoss`: Class implementing the pinball loss.
  - `FocalLoss`: Class implementing the focal loss.

### metric.py
- **Purpose**: Implements evaluation metrics for assessing model performance.
- **Key Components**:
  - `mae`: Mean Absolute Error metric.
  - `inception_score`: Inception Score for evaluating generative models.

### unet.py
- **Purpose**: Implements a basic UNet architecture.
- **Key Components**:
  - UNet implementation for image-to-image translation.

## Guided Diffusion Modules

The `guided_diffusion_modules` directory contains implementations of various UNet architectures used in the diffusion models:

### nn.py
- **Purpose**: Implements neural network building blocks for the UNet architectures.
- **Key Components**:
  - Normalization functions.
  - Attention mechanisms.
  - Utility functions for checkpointing and initialization.

### unet.py
- **Purpose**: Implements the 2D UNet architecture for the diffusion models.
- **Key Components**:
  - `UNet`: Class implementing the 2D UNet architecture.
  - Attention blocks, residual blocks, and up/downsampling layers.

### unet_3d.py
- **Purpose**: Implements the 3D UNet architecture for the vEMDiffuse models.
- **Key Components**:
  - `UNet`: Class implementing the 3D UNet architecture.
  - 3D attention blocks, residual blocks, and up/downsampling layers.

### unet_aleatoric.py and unet_3d_aleatoric.py
- **Purpose**: Implements UNet architectures with aleatoric uncertainty estimation.
- **Key Components**:
  - UNet architectures that output both mean and variance predictions.

### unet_jit.py and unet_jit2.py
- **Purpose**: Implements JIT-compiled versions of the UNet architectures for faster inference.
- **Key Components**:
  - JIT-compatible implementations of the UNet architectures.

## Usage

The models module is used to create and train diffusion models for electron microscopy image enhancement. The main entry points are:

- `create_model`: Used to create a model instance based on configuration.
- `create_EMDiffuse`: Used to create an EMDiffuse model with all components.

## Design Patterns

The models module uses several design patterns:

- **Factory Pattern**: The `create_model`, `define_network`, `define_loss`, and `define_metric` functions are factory functions that create objects based on configuration.
- **Strategy Pattern**: Different loss functions, metrics, and network architectures can be selected based on configuration.
- **Composition**: Models are composed of networks, losses, and metrics.
- **Template Method**: The `BaseModel` class defines the template for model training and inference, while subclasses implement specific behavior.
