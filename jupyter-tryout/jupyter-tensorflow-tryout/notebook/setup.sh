#!/usr/bin/env bash

set -ex

apt-get update
apt-get install -y python3 python3-pip git

pip install tensorflow tensorrt
