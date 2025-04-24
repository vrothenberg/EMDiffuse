# Demo Data

This directory contains demo data for testing the EMDiffuse models. These sample images and volumes can be used to quickly test the functionality of the different EMDiffuse variants without having to download the full datasets.

## Files and Directories

### denoise_demo.tif
- **Purpose**: Demo image for testing the EMDiffuse-n denoising model.
- **Usage**: Can be used as input to the denoising model to demonstrate noise removal.

### super_res_demo.tif
- **Purpose**: Demo image for testing the EMDiffuse-r super-resolution model.
- **Usage**: Can be used as input to the super-resolution model to demonstrate resolution enhancement.

### microns_demo/
- **Purpose**: Demo volume for testing the vEMDiffuse models on MICrONS data.
- **Contents**:
  - `0.tif`: First slice of the demo volume.
  - `1.tif`: Second slice of the demo volume.
- **Usage**: Can be used as input to the vEMDiffuse-a model to demonstrate isotropic reconstruction without isotropic training data.

### mouse_liver_demo/
- **Purpose**: Demo volume for testing the vEMDiffuse models on mouse liver data.
- **Contents**:
  - `0.tif`: First slice of the demo volume.
  - `1.tif`: Second slice of the demo volume.
- **Usage**: Can be used as input to the vEMDiffuse-i model to demonstrate isotropic reconstruction with isotropic training data.

## Usage Examples

### Denoising with EMDiffuse-n

```bash
python run.py -p test -c config/EMDiffuse-n.json --gpu 0 -b 1 --path ./demo/denoise_demo.tif --resume ./experiments/EMDiffuse-n/best --mean 1 --step 1000
```

### Super-Resolution with EMDiffuse-r

```bash
python run.py -p test -c config/EMDiffuse-r.json --gpu 0 -b 1 --path ./demo/super_res_demo.tif --resume ./experiments/EMDiffuse-r/best --mean 1 --step 1000
```

### Isotropic Reconstruction with vEMDiffuse-i

```bash
python run.py -p test -c config/vEMDiffuse-i.json --gpu 0 -b 1 --path ./demo/mouse_liver_demo/ -z 6 --resume ./experiments/vEMDiffuse-i/best --mean 1 --step 200
```

### Isotropic Reconstruction with vEMDiffuse-a

```bash
python run.py -p test -c config/vEMDiffuse-a.json --gpu 0 -b 1 --path ./demo/microns_demo/ -z 6 --resume ./experiments/vEMDiffuse-a/best --mean 1 --step 200
```

## Notes

- The demo data is provided for quick testing and demonstration purposes only.
- For more comprehensive evaluation, it is recommended to use the full datasets as described in the main README.md.
- The demo volumes contain only a few slices, which is sufficient for testing but may not produce optimal results.
- The model weights should be downloaded and placed in the `./experiments` directory before running the examples.
