#!/usr/bin/env bash

set -ex

pip install jupyter

jupyter notebook \
  --allow-root \
  --notebook-dir=notebook \
  --ip='*' \
  --NotebookApp.token='' \
  --NotebookApp.password=''
  