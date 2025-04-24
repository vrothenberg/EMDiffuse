# EMDiffuse-n: Denoising Examples

This directory contains Jupyter notebooks that demonstrate how to use the EMDiffuse-n model for electron microscopy (EM) image denoising.

## Notebooks

### training.ipynb
- **Purpose**: Demonstrates how to train the EMDiffuse-n model on your own data.
- **Key Components**:
  - Data preparation and loading
  - Model configuration
  - Training process
  - Validation and evaluation
  - Model saving

### prediction.ipynb
- **Purpose**: Demonstrates how to use a trained EMDiffuse-n model for inference on new data.
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

Before training the EMDiffuse-n model, you need to prepare your data:

1. **Data Structure**: Your data should be organized as follows:
   ```
   data_root/
     ├── cell_1/
     │   ├── noise_level_1/
     │   │   ├── wf_image1.tif
     │   │   ├── gt_image1.tif
     │   │   └── ...
     │   └── ...
     └── ...
   ```

2. **Registration**: Use the RAFT registration tool to align your noisy and clean images:
   ```bash
   cd RAFT/core
   python register.py --path /path/to/data --tissue YourTissue --patch_size 256 --overlap 0.125
   ```

   Or for custom datasets:
   ```bash
   cd RAFT/core
   python register_custom.py --path /path/to/data --patch_size 256 --overlap 0.125
   ```

## Training

The `training.ipynb` notebook guides you through the process of training the EMDiffuse-n model. Key steps include:

1. **Loading Data**: Loading the prepared dataset.
2. **Configuring the Model**: Setting up the model architecture and training parameters.
3. **Training**: Running the training loop with validation.
4. **Evaluation**: Evaluating the model's performance.
5. **Saving**: Saving the trained model for later use.

## Inference

The `prediction.ipynb` notebook demonstrates how to use a trained EMDiffuse-n model for inference. Key steps include:

1. **Loading the Model**: Loading a pre-trained model.
2. **Preparing Input**: Preparing the noisy input images.
3. **Running Inference**: Using the model to denoise the images.
4. **Visualization**: Visualizing the denoised results.
5. **Saving Results**: Saving the denoised images.

## Example Command

You can also run the training and inference from the command line:

```bash
# Training
python run.py -c config/EMDiffuse-n.json -b 16 --gpu 0,1,2,3 --port 20022 --path /path/to/data --lr 5e-5

# Inference
python run.py -p test -c config/EMDiffuse-n.json --gpu 0 -b 60 --path /path/to/test/data --resume ./experiments/EMDiffuse-n/best --mean 1 --step 1000
```

## Notes

- GPU acceleration is strongly recommended for both training and inference.
- The diffusion model samples one plausible solution from the learned solution distribution. Use the `--mean` parameter to specify the number of samples to generate and average.
- The `--step` parameter controls the number of diffusion steps, with more steps generally leading to higher image quality.
