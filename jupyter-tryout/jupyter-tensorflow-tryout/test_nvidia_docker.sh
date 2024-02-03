#!/usr/bin/env bash

set -ex


docker run --privileged --runtime=nvidia --rm nvidia/cuda:12.3.1-devel-ubuntu20.04 nvidia-smi

# docker pull nvidia/cuda:12.3.1-devel-ubuntu20.04

docker run --privileged --runtime=nvidia --rm nvidia/cuda:12.3.1-devel-ubuntu20.04 nvcc

docker run --privileged --runtime=nvidia --rm agturley/jupyter-tensorflow-cuda-full:master-1831e436 bash
docker run --privileged --runtime=nvidia --rm agturley/jupyter-tensorflow-cuda-full:master-1831e436 nvidia-smi


docker run --privileged --runtime=nvidia --rm \
  -v $PWD:/app \
  -w /app \
  -v ./volumes/.jupyter/jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py \
  --privileged --runtime=nvidia \
  --gpus all \
  -p 3000:3000 \
  -p 8888:8888 \
  agturley/jupyter-tensorflow-cuda-full:master-1831e436 bash
