## StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation

Implementation of StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation (https://arxiv.org/pdf/2011.12799.pdf) in PyTorch

This implementation is mostly relied on rosinality's [stylegan2-pytorch](https://github.com/rosinality/stylegan2-pytorch/)

![An image](./images/stylegan2_kid2_eyes.gif)

## Requirements

I have tested on:

- PyTorch 1.3.1
- CUDA 10.1

## Usage

#### FFHQ

- Firstly, you should download pretrained model from [here](https://www.dropbox.com/s/c3aaq7i6soxmpzu/pretrained_stylegan2_ffhq.tar) and place the `stylegan2-ffhq-config-f.pkl` into `pretrained` folder.
- Open the notebook `StyleSpace_FFHQ.ipynb`

#### Car


#### LSUN



## Credit

The pretrained model weights are from  https://github.com/NVlabs/stylegan2 and converted with https://github.com/rosinality/stylegan2-pytorch

