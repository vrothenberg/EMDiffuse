# vEMDiffuse-a: Isotropic Reconstruction Examples (without Isotropic Training Data)

This directory contains Jupyter notebooks that demonstrate how to use the vEMDiffuse-a model for isotropic reconstruction of volume electron microscopy (vEM) data without requiring isotropic training data.

## Notebooks

### training.ipynb
- **Purpose**: Demonstrates how to train the vEMDiffuse-a model on your own data.
- **Key Components**:
  - Data preparation and loading
  - Model configuration
  - Training process
  - Validation and evaluation
  - Model saving

### prediction.ipynb
- **Purpose**: Demonstrates how to use a trained vEMDiffuse-a model for inference on new data.
- **Key Components**:
  - Loading a pre-trained model
  - Preparing input data
  - Running inference
  - Visualizing and saving results

## Usage

To use these notebooks, you need to have Jupyter installed in your conda environment:

```bash
pip install jupyter
```

Then, start Jupyter and open the desired notebook:

```bash
jupyter notebook
```

## Data Preparation

Before training the vEMDiffuse-a model, you need to prepare your data:

1. **Data Structure**: Your data should be organized as follows:
   ```
   vEM_data/
     ├── 0.tif  # First slice
     ├── 1.tif  # Second slice
     ├── ...
     └── n.tif  # Last slice
   ```

   The data can be an anisotropic volume, meaning that the resolution along the z-axis is lower than along the x and y axes.

2. **Preprocessing**: Slice along the YZ view to prepare the data for training:
   ```bash
   python vEMa_pre.py --path ./vEM_data
   ```

## Training

The `training.ipynb` notebook guides you through the process of training the vEMDiffuse-a model. Key steps include:

1. **Loading Data**: Loading the prepared dataset.
2. **Configuring the Model**: Setting up the model architecture and training parameters.
3. **Training**: Running the training loop with validation.
4. **Evaluation**: Evaluating the model's performance.
5. **Saving**: Saving the trained model for later use.

## Inference

The `prediction.ipynb` notebook demonstrates how to use a trained vEMDiffuse-a model for inference. Key steps include:

1. **Loading the Model**: Loading a pre-trained model.
2. **Preparing Input**: Preparing the anisotropic input volume.
3. **Running Inference**: Using the model to reconstruct an isotropic volume.
4. **Visualization**: Visualizing the reconstructed volume.
5. **Saving Results**: Saving the isotropic volume.

## Example Command

You can also run the training and inference from the command line:

```bash
# Preprocessing
python vEMa_pre.py --path ./vEM_data

# Training
python run.py -c config/vEMDiffuse-a.json -b 16 --gpu 0,1,2,3 --port 20022 --path ./vEM_data/transposed -z 6 --lr 5e-5

# Inference
python run.py -p test -c config/vEMDiffuse-a.json --gpu 0 -b 16 --path ./vEM_test_data/ -z 6 --resume ./experiments/vEMDiffuse-a/best --mean 1 --step 200
```

## Notes

- GPU acceleration is strongly recommended for both training and inference.
- The `-z` parameter specifies the subsampling factor of the Z axis. For example, to reconstruct an 8 nm x 8 nm x 8 nm volume from an 8 nm x 8 nm x 48 nm volume, the subsampling factor should be 6.
- The diffusion model samples one plausible solution from the learned solution distribution. Use the `--mean` parameter to specify the number of samples to generate and average.
- The `--step` parameter controls the number of diffusion steps, with more steps generally leading to higher quality reconstruction.
- The vEMDiffuse-a model is designed for cases where you don't have isotropic training data available. It uses a novel approach to learn the isotropic reconstruction from anisotropic data only.
- Experiments on anisotropic volumes with fewer layers (e.g., 128 layers) are now possible. Given the input size of 256, the anisotropic volume is duplicated along the axial axis before proceeding with vEMDiffuse-a training.
