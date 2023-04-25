#!/usr/bin/env bash

set -ex

jupyter-notebook \
    --allow-root \
    --ip=0.0.0.0
