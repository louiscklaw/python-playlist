#!/usr/bin/env bash

set -ex

docker run -it \
  -v $PWD:/app \
  -w /app \
  -v ~/.ssh/id_rsa:/home/node/.ssh/id_rsa:ro \
  -v ~/.ssh/known_host:/home/node/.ssh/known_hosts:ro \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ./volumes/.jupyter/jupyter_notebook_config.py:/root/.jupyter/jupyter_notebook_config.py \
  -p 3000:3000 \
  -p 8888:8888 \
  --rm \
  python:latest \
  bash
