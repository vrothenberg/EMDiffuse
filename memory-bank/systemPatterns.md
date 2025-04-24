# EMDiffuse System Patterns

## System Architecture

The EMDiffuse project follows a modular architecture that separates concerns and promotes code reuse. The architecture consists of several key components:

### Core Components

1. **Core Module**: Provides base classes and utilities that are used throughout the project.
   - `BaseModel`: Abstract base class for all models.
   - `BaseNetwork`: Abstract base class for all neural networks.
   - `BaseDataset`: Abstract base class for all datasets.
   - Utility functions for common operations.

2. **Models Module**: Implements the diffusion models for various tasks.
   - `EMDiffuse_model.py`: Implements the EMDiffuse model for 2D image enhancement.
   - `EMDiffuse_network.py`: Implements the network architecture for EMDiffuse.
   - `vEMDiffuse_model.py`: Implements the vEMDiffuse model for 3D volume enhancement.
   - `vEMDiffuse_network.py`: Implements the network architecture for vEMDiffuse.
   - `guided_diffusion_modules`: Implements the UNet architectures used in the diffusion models.

3. **Data Module**: Implements dataset classes for loading and processing data.
   - `dataset.py`: Implements dataset classes for various tasks.
   - `util`: Provides utility functions for data augmentation and processing.

4. **Config Module**: Contains JSON configuration files for the different model variants.
   - `EMDiffuse-n.json`: Configuration for the EMDiffuse-n model for denoising.
   - `EMDiffuse-r.json`: Configuration for the EMDiffuse-r model for super-resolution.
   - `vEMDiffuse-i.json`: Configuration for the vEMDiffuse-i model for isotropic reconstruction with isotropic training data.
   - `vEMDiffuse-a.json`: Configuration for the vEMDiffuse-a model for isotropic reconstruction without isotropic training data.

5. **RAFT Module**: Implements image registration and alignment for data preparation.
   - `register.py`: Implements image registration for the EMDiffuse-n denoising task.
   - `super_res_register.py`: Implements image registration for the EMDiffuse-r super-resolution task.
   - `register_custom.py`: Implements custom image registration for user-provided datasets.

6. **3D-SR-Unet Module**: Implements a 3D Super-Resolution U-Net as an alternative approach to vEMDiffuse.
   - `model.py`: Implements the 3D-SR-Unet architecture.
   - `train.py`: Implements the training loop for the 3D-SR-Unet.
   - `data.py`: Implements dataset classes for the 3D-SR-Unet.

### Execution Flow

The execution flow of the EMDiffuse project follows a typical machine learning workflow:

1. **Data Preparation**: Raw data is processed and prepared for training and inference.
   - For EMDiffuse-n and EMDiffuse-r, this involves registering and aligning image pairs using the RAFT module.
   - For vEMDiffuse-i and vEMDiffuse-a, this involves preparing volume data.

2. **Model Configuration**: The model is configured using JSON configuration files.
   - Configuration files specify the model architecture, training parameters, and dataset settings.
   - Command-line arguments can override specific configuration parameters.

3. **Training**: The model is trained on the prepared data.
   - The `run.py` script is used to train the model with the specified configuration.
   - Training progress is logged and visualized using TensorBoard.

4. **Inference**: The trained model is used for inference on new data.
   - The `run.py` script is used for inference with the `-p test` flag.
   - Results are saved and can be visualized.

## Design Patterns

The EMDiffuse project employs several design patterns to promote code reuse, maintainability, and extensibility:

### Factory Pattern

The factory pattern is used to create objects based on configuration. The `init_obj` function in `core/praser.py` is a factory function that creates objects from configuration:

```python
def init_obj(opt, logger, default_file_name=None, init_type=None, *args, **kwargs):
    """
    finds a function handle with the name given as 'name' in config,
    and returns the instance initialized with corresponding args.
    """
    # ...
    return obj_class(*args, **kwargs, **opt['args'])
```

This allows for flexible object creation based on configuration, enabling easy experimentation with different model architectures, loss functions, and datasets.

### Strategy Pattern

The strategy pattern is used to select different algorithms or approaches at runtime. For example, different loss functions, metrics, and network architectures can be selected based on configuration:

```python
def define_loss(logger, loss_opt):
    return init_obj(loss_opt, logger, default_file_name='models.loss', init_type='Loss')

def define_metric(logger, metric_opt):
    return init_obj(metric_opt, logger, default_file_name='models.metric', init_type='Metric')

def define_network(logger, opt, network_opt):
    net = init_obj(network_opt, logger, default_file_name='models.network', init_type='Network')
    # ...
    return net
```

This allows for easy swapping of components without changing the core code.

### Template Method Pattern

The template method pattern is used to define the skeleton of an algorithm in a method, deferring some steps to subclasses. The `BaseModel` class defines the template for model training and inference, while subclasses implement specific behavior:

```python
class BaseModel:
    def train(self):
        self.model_train()
        # ...

    def model_train(self):
        raise NotImplementedError('model_train must be implemented by subclass')
```

This allows for consistent behavior across different model implementations while allowing for customization.

### Observer Pattern

The observer pattern is used for logging and visualization. The `InfoLogger` and `VisualWriter` classes act as observers that are notified of events during training and inference:

```python
class InfoLogger:
    def info(self, msg):
        # ...

class VisualWriter:
    def add_scalar(self, tag, scalar_value, step):
        # ...
```

This allows for decoupled logging and visualization without affecting the core training and inference code.

### Composition

Composition is used extensively throughout the project to build complex objects from simpler ones. For example, models are composed of networks, losses, and metrics:

```python
def create_model(**cfg_model):
    # ...
    model = init_obj(model_opt, logger, default_file_name='models.model', init_type='Model')
    return model
```

This allows for flexible and modular construction of complex objects.

## Component Relationships

The relationships between the key components of the EMDiffuse project can be visualized as follows:

```
+----------------+     +----------------+     +----------------+
|     Core       |<----+     Models     |<----+     Data       |
+----------------+     +----------------+     +----------------+
        ^                     ^                     ^
        |                     |                     |
        v                     v                     v
+----------------+     +----------------+     +----------------+
|     Config     |---->|     run.py     |---->|     RAFT       |
+----------------+     +----------------+     +----------------+
                              ^
                              |
                              v
                       +----------------+
                       |   3D-SR-Unet   |
                       +----------------+
```

- The **Core** module provides base classes and utilities used by all other modules.
- The **Models** module implements the diffusion models, extending the base classes from the Core module.
- The **Data** module implements dataset classes for loading and processing data, also extending base classes from the Core module.
- The **Config** module contains configuration files that are used by the `run.py` script to configure the models and datasets.
- The **run.py** script is the main entry point for training and inference, using components from the Models and Data modules.
- The **RAFT** module is used for data preparation, particularly for registering and aligning image pairs.
- The **3D-SR-Unet** module provides an alternative approach to vEMDiffuse for 3D super-resolution.

## Code Organization

The code is organized into directories that correspond to the key components of the system:

```
EMDiffuse/
├── core/                # Core module with base classes and utilities
├── models/              # Models module with diffusion model implementations
│   └── guided_diffusion_modules/  # UNet architectures for diffusion models
├── data/                # Data module with dataset implementations
│   └── util/            # Utility functions for data augmentation and processing
├── config/              # Configuration files for different model variants
├── RAFT/                # RAFT module for image registration and alignment
│   └── core/            # Core implementation of RAFT
├── 3D-SR-Unet/          # 3D-SR-Unet module as an alternative approach
├── example/             # Example notebooks for using the models
│   ├── denoise/         # Examples for EMDiffuse-n
│   ├── super-res/       # Examples for EMDiffuse-r
│   ├── vEMDiffuse-i/    # Examples for vEMDiffuse-i
│   └── vEMDiffuse-a/    # Examples for vEMDiffuse-a
├── demo/                # Demo data for testing
└── run.py               # Main entry point for training and inference
```

This organization promotes modularity and separation of concerns, making it easier to understand, maintain, and extend the codebase.

## Extensibility

The EMDiffuse project is designed to be extensible in several ways:

1. **New Model Variants**: New model variants can be created by extending the base classes and implementing specific behavior.
2. **New Network Architectures**: New network architectures can be implemented and used with the existing models.
3. **New Loss Functions and Metrics**: New loss functions and metrics can be implemented and used with the existing models.
4. **New Dataset Classes**: New dataset classes can be implemented for different types of data.
5. **New Configuration Files**: New configuration files can be created for different experimental settings.

This extensibility allows researchers to build upon the existing codebase and adapt it to their specific needs.

## Deployment Considerations

The EMDiffuse project is primarily designed for research use, but it can be deployed in various ways:

1. **Local Installation**: Users can install the project locally and use it for their own research.
2. **Cluster Deployment**: The project can be deployed on a compute cluster for large-scale training and inference.
3. **Docker Containerization**: The project can be containerized using Docker for easier deployment and reproducibility.
4. **Cloud Deployment**: The project can be deployed on cloud platforms for scalable training and inference.

The modular architecture and configuration-based approach make it easier to adapt the project to different deployment scenarios.
