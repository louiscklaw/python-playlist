# https://github.com/facebookresearch/nougat/blob/47c77d70727558b4a2025005491ecb26ee97f523/docker/Dockerfile#L3
FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get -y install python3-pip git

RUN mkdir workspace
WORKDIR /workspace

RUN pip install jupyter

RUN pip install tensorflow
RUN pip install tensorrt

# ENTRYPOINT sleep infinity

# ENTRYPOINT jupyter notebook \
#   --allow-root \
#   --notebook-dir=/workspace \
#   --ip='*' \
#   --NotebookApp.token='' \
#   --NotebookApp.password=''
