# Data Utility Functions

This directory contains utility functions for data augmentation and processing in the EMDiffuse project.

## Files and Functionality

### auto_augment.py
- **Purpose**: Provides functions for automatic data augmentation.
- **Key Components**:
  - `AutoAugment`: Class for applying automatic augmentation policies to images.
  - `ImageNetAutoAugment`: Class for applying ImageNet-specific augmentation policies.
  - Various image transformation functions:
    - `shear_x`, `shear_y`: Functions for applying shear transformations.
    - `translate_x`, `translate_y`: Functions for applying translation transformations.
    - `rotate`: Function for rotating images.
    - `auto_contrast`, `invert`, `equalize`: Functions for adjusting image contrast and colors.
    - `solarize`, `posterize`: Functions for applying special effects to images.
    - `contrast`, `color`, `brightness`, `sharpness`: Functions for adjusting image properties.
    - `cutout`: Function for applying cutout augmentation.

### mask.py
- **Purpose**: Provides functions for creating and applying masks to images.
- **Key Components**:
  - `random_cropping_bbox`: Function for generating random cropping bounding boxes.
  - `random_bbox`: Function for generating random bounding boxes for masks.
  - `bbox2mask`: Function for converting bounding boxes to masks.
  - `brush_stroke_mask`: Function for generating free-form masks using brush strokes.
  - `random_irregular_mask`: Function for generating random irregular masks.
  - `get_irregular_mask`: Function for getting irregular masks with constraints on mask ratio.

## Usage

These utility functions are used by the dataset classes in the data module for data augmentation and processing. They provide various ways to transform and augment images, as well as to create masks for training and inference.

### Data Augmentation

The `auto_augment.py` file provides functions for applying various data augmentation techniques to images. These techniques include:

- **Geometric Transformations**: Shearing, translation, rotation.
- **Color Transformations**: Contrast adjustment, color adjustment, brightness adjustment, sharpness adjustment.
- **Special Effects**: Solarization, posterization, inversion, equalization.
- **Cutout**: Random removal of image patches.

The augmentation policies are defined as sequences of these transformations, with each transformation having a probability of being applied and a magnitude parameter.

### Mask Generation

The `mask.py` file provides functions for generating various types of masks for training and inference. These include:

- **Bounding Box Masks**: Rectangular masks defined by a bounding box.
- **Brush Stroke Masks**: Free-form masks generated using brush strokes.
- **Irregular Masks**: Random irregular masks with constraints on mask ratio.

These masks can be used for tasks such as inpainting, where parts of an image are masked out and the model is trained to reconstruct the masked regions.

## Examples

### Using AutoAugment

```python
from data.util.auto_augment import AutoAugment

# Create an AutoAugment instance
augmenter = AutoAugment()

# Apply augmentation to an image
augmented_image = augmenter(image)
```

### Generating a Mask

```python
from data.util.mask import random_bbox, bbox2mask

# Generate a random bounding box
bbox = random_bbox(img_shape=(256, 256))

# Convert the bounding box to a mask
mask = bbox2mask(img_shape=(256, 256), bbox=bbox)
