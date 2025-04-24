# EMDiffuse

This repository contains the official PyTorch implementation of the paper: **EMDiffuse: A Diffusion-based Deep Learning Method Augmenting Ultrastructural Imaging and Volume Electron Microscopy** accepted by [Nature Communications](https://www.nature.com/articles/s41467-024-49125-z).

EMDiffuse offers a toolkit for applying diffusion models to electron microscopy (EM) images, designed to enhance ultrastructural imaging in EM and extend the capabilities of volume electron microscopy (vEM). We have tailored the diffusion model for EM applications, developing **EMDiffuse-n** for EM denoising, **EMDiffuse-r** for EM super-resolution, and **vEMDiffuse-i** and **vEMDiffuse-a** for generating isotropic resolution data from anisotropic volumes in vEM.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Model Variants](#model-variants)
- [Usage](#usage)
  - [Denoising](#denoising)
  - [Super-Resolution](#super-resolution)
  - [Isotropic Reconstruction](#isotropic-reconstruction)
- [Examples](#examples)
- [Documentation](#documentation)
- [Model Weights](#model-weights)
- [Citation](#citation)
- [Contact](#contact)

## Overview

EMDiffuse is a diffusion-based deep learning method for enhancing electron microscopy images. It offers several variants for different tasks:

- **EMDiffuse-n**: For EM denoising, removing noise from EM images to reveal clearer ultrastructural details.
- **EMDiffuse-r**: For EM super-resolution, enhancing the resolution of EM images to reveal finer details.
- **vEMDiffuse-i**: For generating isotropic resolution data from anisotropic volumes in vEM, using isotropic training data.
- **vEMDiffuse-a**: For generating isotropic resolution data from anisotropic volumes in vEM, without requiring isotropic training data.

## Installation

Please install PyTorch (=1.13) before you run the code. We strongly recommend you install Anaconda3, where we use Python 3.8.

```bash
conda create --name emdiffuse python=3.8
conda activate emdiffuse
pip install -r requirements.txt
```

## Model Variants

### EMDiffuse-n

EMDiffuse-n is designed for EM denoising. It takes a noisy EM image as input and produces a denoised image as output. The model is trained on paired noisy and clean images.

### EMDiffuse-r

EMDiffuse-r is designed for EM super-resolution. It takes a low-resolution EM image as input and produces a high-resolution image as output. The model is trained on paired low-resolution and high-resolution images.

### vEMDiffuse-i

vEMDiffuse-i is designed for isotropic reconstruction of vEM data using isotropic training data. It takes an anisotropic volume as input and produces an isotropic volume as output. The model is trained on isotropic volumes.

### vEMDiffuse-a

vEMDiffuse-a is designed for isotropic reconstruction of vEM data without requiring isotropic training data. It takes an anisotropic volume as input and produces an isotropic volume as output. The model is trained on anisotropic volumes only.

## Usage

### Denoising

#### Training

1. **Prepare Data**: Register and crop patches for model training.
   ```bash
   cd RAFT/core
   python register.py --path /data/EMDiffuse_dataset/brain_train --tissue Brain --patch_size 256 --overlap 0.125
   ```

2. **Train Model**:
   ```bash
   python run.py -c config/EMDiffuse-n.json -b 16 --gpu 0,1,2,3 --port 20022 --path /data/EMDiffuse_dataset/brain_train/denoise/train_wf --lr 5e-5
   ```

#### Inference

1. **Crop Image**:
   ```bash
   python test_pre.py --path /data/EMDiffuse_dataset/brain_test --task denoise
   ```

2. **Testing**:
   ```bash
   python run.py -p test -c config/EMDiffuse-n.json --gpu 0 -b 60 --path /data/EMDiffuse_dataset/brain_test/denoise_test_crop_patches --resume ./experiments/EMDiffuse-n/best --mean 1 --step 1000
   ```

### Super-Resolution

#### Training

1. **Prepare Data**: Register and crop patches for model training.
   ```bash
   cd RAFT/core
   python super_res_register.py --path /data/EMDiffuse_dataset/brain_train --patch_size 128 --overlap 0.125
   ```

2. **Train Model**:
   ```bash
   python run.py -c config/EMDiffuse-r.json -b 16 --gpu 0,1,2,3 --port 20022 --path /data/EMDiffuse_dataset/brain_train/zoom/train_wf --lr 5e-5
   ```

#### Inference

1. **Crop Image**:
   ```bash
   python test_pre.py --path /data/EMDiffuse_dataset/brain_test --task super
   ```

2. **Testing**:
   ```bash
   python run.py -p test -c config/EMDiffuse-r.json --gpu 0 -b 60 --path /data/EMDiffuse_dataset/brain_test/super_test_crop_patches --resume ./experiments/EMDiffuse-r/best --mean 1 --step 1000
   ```

### Isotropic Reconstruction

#### Training vEMDiffuse-i with Isotropic Training Data

```bash
python run.py -c config/vEMDiffuse-i.json -b 16 --gpu 0,1,2,3 --port 20022 --path ./vEM_data -z 6 --lr 5e-5
```

#### Training vEMDiffuse-a without Isotropic Training Data

1. **Slice along YZ view**:
   ```bash
   python vEMa_pre.py --path ./vEM_data
   ```

2. **Train Model**:
   ```bash
   python run.py -c config/vEMDiffuse-a.json -b 16 --gpu 0,1,2,3 --port 20022 --path ./vEM_data/transposed -z 6 --lr 5e-5
   ```

#### Inference

```bash
python run.py -p test -c config/vEMDiffuse-i.json --gpu 0 -b 16 --path ./vEM_test_data/ -z 6 --resume ./experiments/vEMDiffuse-i/best --mean 1 --step 200
```

## Examples

We provide Jupyter notebooks for step-by-step tutorials:

- [2D EM denoising](example/denoise/)
- [2D EM super-resolution](example/super-res/)
- [Isotropic vEM reconstruction with isotropic training data](example/vEMDiffuse-i/)
- [Isotropic vEM reconstruction without isotropic training data](example/vEMDiffuse-a/)

To run the notebooks, install Jupyter in your conda environment or use [Google Colab](https://colab.research.google.com/).

```bash
pip install jupyter
```

## Documentation

We have provided detailed documentation for each module in the repository:

- [Core Module](core/README.md): Base classes and utilities.
- [Models Module](models/README.md): Model implementations.
- [Data Module](data/README.md): Dataset implementations.
- [Config Files](config/README.md): Configuration files.
- [3D-SR-Unet](3D-SR-Unet/README.md): 3D Super-Resolution U-Net implementation.
- [RAFT Core](RAFT/core/README.md): Image registration and alignment.
- [Demo Data](demo/README.md): Demo data for testing.
- [Example Notebooks](example/README.md): Example usage.

## Model Weights

A selection of model weights is available at [EMDiffuse_model_weight](https://connecthkuhk-my.sharepoint.com/:f:/g/personal/u3590540_connect_hku_hk/EtSvqrIyrNREim5dJfabx2ABMLNhwk2Z9EsJDD4w6mls8g?e=OdP4Vq). Download them and place them in the `./experiments` folder.

The vEMDiffuse-i model was trained on the [Openorgnelle liver dataset](https://doi.org/10.25378/janelia.16913047.v1). And vEMDiffuse-a was trained on the [MICrONS multi-area dataset](https://www.microns-explorer.org/).

All results, including training and inference, will be stored in a newly created folder under `./experiments`.

Running the diffusion process on a **GPU** is highly recommended for both training and testing.

## Citation

If you find this work useful for your research, please cite our paper:

```
@article{lu2024emdiffuse,
  title={EMDiffuse: A Diffusion-based Deep Learning Method Augmenting Ultrastructural Imaging and Volume Electron Microscopy},
  author={Lu, Chenxin and Jiang, Haibo},
  journal={Nature Communications},
  year={2024}
}
```

## Contact

For more information, please visit our webpage: https://www.haibojianglab.com/emdiffuse.

Should you have any questions regarding the code, please do not hesitate to contact us.
