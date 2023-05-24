# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_fad_gen.ipynb.

# %% auto 0
__all__ = ['gen', 'main']

# %% ../nbs/01_fad_gen.ipynb 4
import argparse

# %% ../nbs/01_fad_gen.ipynb 5
def gen(model_ckpt, data_source, n=256):
    print(model_ckpt, data_source, n)

# %% ../nbs/01_fad_gen.ipynb 6
def main(): 
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('model_ckpt', help='Model checkpoint')
    parser.add_argument('data_source', help='string listing S3 resources for data')
    parser.add_argument('--n', type=int, default=256, help='Number of real/fake samples to grab/generate, respectively')
    parser.add_argument('--sr', type=int, default=48000, help='sample rate (will resample inputs at this rate)')
    args = parser.parse_args()
    gen( args.model_ckpt, args.data_source, n=args.n)
