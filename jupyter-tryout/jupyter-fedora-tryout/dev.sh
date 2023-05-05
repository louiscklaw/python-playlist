#!/usr/bin/env bash

set -ex

pip install jupyter

jupyter notebook \
  --allow-root \
  --ip=0.0.0.0 \
  --notebook-dir=notebook
