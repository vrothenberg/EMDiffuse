# Example Notebooks

This directory contains Jupyter notebooks that demonstrate how to use the EMDiffuse models for various tasks. These notebooks provide step-by-step tutorials for training and using the different variants of EMDiffuse.

## Directories and Notebooks

### denoise/
- **Purpose**: Examples for the EMDiffuse-n model for EM denoising.
- **Notebooks**:
  - `training.ipynb`: Demonstrates how to train the EMDiffuse-n model.
  - `prediction.ipynb`: Demonstrates how to use the trained EMDiffuse-n model for inference.

### super-res/
- **Purpose**: Examples for the EMDiffuse-r model for EM super-resolution.
- **Notebooks**:
  - `training.ipynb`: Demonstrates how to train the EMDiffuse-r model.
  - `prediction.ipynb`: Demonstrates how to use the trained EMDiffuse-r model for inference.

### vEMDiffuse-i/
- **Purpose**: Examples for the vEMDiffuse-i model for isotropic reconstruction with isotropic training data.
- **Notebooks**:
  - `training.ipynb`: Demonstrates how to train the vEMDiffuse-i model.
  - `prediction.ipynb`: Demonstrates how to use the trained vEMDiffuse-i model for inference.

### vEMDiffuse-a/
- **Purpose**: Examples for the vEMDiffuse-a model for isotropic reconstruction without isotropic training data.
- **Notebooks**:
  - `training.ipynb`: Demonstrates how to train the vEMDiffuse-a model.
  - `prediction.ipynb`: Demonstrates how to use the trained vEMDiffuse-a model for inference.

## Usage

To use these notebooks, you need to have Jupyter installed in your conda environment:

```bash
pip install jupyter
```

Alternatively, you can use Google Colab to run these notebooks.

### Running Locally

1. Navigate to the example directory:
   ```bash
   cd example
   ```

2. Start Jupyter:
   ```bash
   jupyter notebook
   ```

3. Open the desired notebook in your browser.

### Running on Google Colab

1. Upload the notebook to Google Colab.
2. Follow the instructions in the notebook to set up the environment and run the code.

## Notes

- The training notebooks assume that you have prepared the training data as described in the main README.md.
- The prediction notebooks assume that you have downloaded the pre-trained model weights and placed them in the appropriate directory.
- The notebooks include detailed comments and explanations to guide you through the process.
- You may need to modify the file paths in the notebooks to match your specific setup.
- GPU acceleration is strongly recommended for both training and inference.
