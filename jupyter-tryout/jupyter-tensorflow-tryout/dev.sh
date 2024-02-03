#!/usr/bin/env bash

set -ex

# test cuda / nvidia present
nvidia-smi

pip install jupyter

rm -rf **/.ipynb_checkpoints

jupyter notebook \
  --allow-root \
  --notebook-dir=notebook \
  --ip='*' \
  --NotebookApp.token='' \
  --NotebookApp.password=''
  