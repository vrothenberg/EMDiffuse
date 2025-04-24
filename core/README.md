# Core Module

The Core module provides the foundational classes and utilities for the EMDiffuse project. It contains base classes that are extended by other modules, as well as utility functions for common operations.

## Files and Functionality

### base_dataset.py
- **Purpose**: Provides the base dataset class for loading and processing image data.
- **Key Components**:
  - `BaseDataset`: Abstract class that implements common dataset functionality.
  - `make_dataset`: Function to create a list of image paths.
  - `is_image_file`: Function to check if a file is an image.
  - `pil_loader`: Function to load an image using PIL.

### base_model.py
- **Purpose**: Provides the base model class for all models in the project.
- **Key Components**:
  - `BaseModel`: Abstract class that implements common model functionality such as training, validation, saving/loading models, and managing optimizers and schedulers.
  - `CustomResult`: Named tuple for storing results.

### base_network.py
- **Purpose**: Provides the base network class for all neural networks in the project.
- **Key Components**:
  - `BaseNetwork`: Abstract class that extends PyTorch's nn.Module and implements weight initialization methods.

### calibration.py
- **Purpose**: Provides functions for model calibration, particularly for uncertainty estimation.
- **Key Components**:
  - `fraction_missed_loss`: Function to calculate the fraction of ground truth values outside the predicted bounds.
  - `get_rcps_losses_from_outputs`: Function to calculate risk-controlling prediction sets losses.
  - `calibrate_model`: Function to calibrate a model's uncertainty estimates.

### logger.py
- **Purpose**: Provides logging functionality for the project.
- **Key Components**:
  - `InfoLogger`: Class for logging text information to files and console.
  - `VisualWriter`: Class for logging visual information to TensorBoard and saving images.
  - `LogTracker`: Class for tracking and computing metrics during training.

### praser.py
- **Purpose**: Provides functionality for parsing configuration files and command-line arguments.
- **Key Components**:
  - `parse`: Function to parse configuration files and command-line arguments.
  - `init_obj`: Function to initialize objects from configuration.
  - `dict_to_nonedict`: Function to convert dictionaries to NoneDict, which returns None for missing keys.

### util.py
- **Purpose**: Provides utility functions for common operations.
- **Key Components**:
  - `tensor2img`: Function to convert a tensor to a numpy image.
  - `postprocess`: Function to postprocess a list of images.
  - `set_seed`: Function to set random seeds for reproducibility.
  - `set_device`: Function to move tensors to the appropriate device (CPU/GPU).

## Usage

The core module is used by other modules in the project. For example:

- The `models` module extends `BaseModel` and `BaseNetwork` to implement specific model architectures.
- The `data` module extends `BaseDataset` to implement specific dataset loaders.
- The `logger` module is used throughout the project for logging information.
- The `util` module provides utility functions used throughout the project.

## Design Patterns

The core module uses several design patterns:

- **Abstract Base Classes**: `BaseModel`, `BaseNetwork`, and `BaseDataset` are abstract base classes that define interfaces and common functionality.
- **Factory Pattern**: `init_obj` in `praser.py` is a factory function that creates objects from configuration.
- **Singleton Pattern**: Loggers are often implemented as singletons to ensure a single logging instance.
- **Strategy Pattern**: Different initialization strategies can be selected in `BaseNetwork`.
