#!/usr/bin/env bash

set -ex

# Start a TensorFlow Docker container
# docker pull tensorflow/tensorflow                     # latest stable release
# docker pull tensorflow/tensorflow:devel-gpu           # nightly dev release w/ GPU support
# docker pull tensorflow/tensorflow:latest-gpu-jupyter  # latest release w/ GPU support and Jupyter

# 
# docker run -it --rm tensorflow/tensorflow \
#    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
# docker run -it tensorflow/tensorflow bash
# docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python ./script.py
# docker run -it -p 8888:8888 tensorflow/tensorflow:nightly-jupyter

# GPU support
# docker run --gpus all --rm nvidia/cuda nvidia-smi

# Examples using GPU-enabled images
# docker run -it --privileged --runtime=nvidia --gpus all --rm tensorflow/tensorflow:latest-gpu \
#    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# docker run -it \
#   --gpus all tensorflow/tensorflow:latest-gpu-jupyter bash
docker run -it --rm -v $PWD:/tmp -w /tmp --privileged --runtime=nvidia --gpus all \
  -p 8888:8888 \
  -v ./volumes/.jupyter/jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py \
  tensorflow/tensorflow:latest-gpu-jupyter
