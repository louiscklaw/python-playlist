#!/usr/bin/env bash

set -ex

docker run -it \
  -v $PWD:/app \
  -w /app \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.ssh/id_rsa:/home/node/.ssh/id_rsa:ro \
  -v ~/.ssh/known_host:/home/node/.ssh/known_hosts:ro \
  -p 8888:8888 \
  --rm \
  python:3.10 \
  bash

  # -u 1000:1000 \
  # -e XDG_CACHE_HOME=/app/.cache \
