# Guided Diffusion Modules

This directory contains the implementation of various UNet architectures used in the diffusion models of the EMDiffuse project. These architectures are based on the guided diffusion approach and are used for both 2D and 3D image enhancement tasks.

## Files and Functionality

### nn.py
- **Purpose**: Implements neural network building blocks and utility functions for the UNet architectures.
- **Key Components**:
  - `normalization`: Function to create normalization layers (GroupNorm).
  - `zero_module`: Function to zero-initialize the weights of a module.
  - `checkpoint`: Function for gradient checkpointing to save memory.
  - `gamma_embedding`: Function to create sinusoidal embeddings for timesteps.
  - Utility functions for counting FLOPs and other operations.

### unet.py
- **Purpose**: Implements the 2D UNet architecture for the diffusion models.
- **Key Components**:
  - `UNet`: Class implementing the 2D UNet architecture.
  - `AttentionBlock`: Self-attention mechanism for capturing long-range dependencies.
  - `ResBlock`: Residual block with time embedding for the UNet.
  - `Upsample` and `Downsample`: Classes for up and downsampling operations.
  - `QKVAttention`: Query-Key-Value attention mechanism.

### unet_3d.py
- **Purpose**: Implements the 3D UNet architecture for the vEMDiffuse models.
- **Key Components**:
  - `UNet`: Class implementing the 3D UNet architecture.
  - `AttentionBlock`: Self-attention mechanism adapted for 3D data.
  - `ResBlock`: Residual block with time embedding for the 3D UNet.
  - `Upsample` and `Downsample`: Classes for up and downsampling operations in 3D.
  - `QKVAttention`: Query-Key-Value attention mechanism for 3D data.

### unet_aleatoric.py
- **Purpose**: Implements a 2D UNet architecture with aleatoric uncertainty estimation.
- **Key Components**:
  - `UNet`: Class implementing the 2D UNet architecture with variance prediction.
  - Similar components to unet.py but with additional outputs for uncertainty.

### unet_3d_aleatoric.py
- **Purpose**: Implements a 3D UNet architecture with aleatoric uncertainty estimation.
- **Key Components**:
  - `UNet`: Class implementing the 3D UNet architecture with variance prediction.
  - Similar components to unet_3d.py but with additional outputs for uncertainty.

### unet_jit.py and unet_jit2.py
- **Purpose**: Implements JIT-compiled versions of the UNet architectures for faster inference.
- **Key Components**:
  - JIT-compatible implementations of the UNet architectures.
  - Optimized for inference speed.

## Architecture Details

### UNet Architecture

The UNet architecture is a popular choice for image-to-image translation tasks. It consists of:

1. **Encoder Path (Downsampling)**:
   - A series of convolutional blocks that progressively reduce the spatial dimensions while increasing the feature channels.
   - Each block typically includes convolution, normalization, and activation.
   - Downsampling is performed using strided convolutions or pooling.

2. **Bottleneck**:
   - The middle part of the network with the highest feature channel count and lowest spatial dimensions.
   - Often includes attention mechanisms to capture global context.

3. **Decoder Path (Upsampling)**:
   - A series of convolutional blocks that progressively increase the spatial dimensions while decreasing the feature channels.
   - Each block typically includes convolution, normalization, and activation.
   - Upsampling is performed using transposed convolutions or interpolation.
   - Skip connections from the encoder path are used to preserve spatial information.

4. **Time Embedding**:
   - In diffusion models, the UNet takes an additional input representing the noise level or timestep.
   - This is embedded using sinusoidal embeddings and injected into each block of the network.

### Attention Mechanism

The attention mechanism in these UNet architectures is based on self-attention:

1. **Query, Key, Value (QKV) Computation**:
   - The input features are projected to create query, key, and value tensors.

2. **Attention Weights Computation**:
   - The attention weights are computed as the scaled dot product of queries and keys.
   - The weights are normalized using softmax.

3. **Output Computation**:
   - The output is computed as the weighted sum of values, using the attention weights.

### Residual Blocks

The residual blocks in these UNet architectures include:

1. **Normalization and Activation**:
   - GroupNorm followed by SiLU (Sigmoid Linear Unit) activation.

2. **Time Embedding Injection**:
   - The time embedding is processed and added to the features.

3. **Convolution**:
   - Convolutional layers with skip connections.

4. **Scale-Shift Normalization**:
   - A FiLM-like conditioning mechanism where the time embedding is used to generate scale and shift parameters for normalization.

## Usage

These UNet architectures are used as the backbone of the diffusion models in the EMDiffuse project. They are instantiated and configured through the `define_network` function in the models module, based on the configuration provided in the JSON configuration files.

## References

The implementation is based on the guided diffusion approach, which is described in the following papers:

- "Denoising Diffusion Probabilistic Models" by Ho et al.
- "Improved Denoising Diffusion Probabilistic Models" by Nichol and Dhariwal.
- "Diffusion Models Beat GANs on Image Synthesis" by Dhariwal and Nichol.
