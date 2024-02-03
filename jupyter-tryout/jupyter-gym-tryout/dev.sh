#!/usr/bin/env bash

set -ex

pip install jupyter
pip install gym 
pip install gym-retro

pushd roms
  python -m retro.import .
popd

jupyter notebook \
  --allow-root \
  --ip=0.0.0.0 \
  --notebook-dir=notebook
