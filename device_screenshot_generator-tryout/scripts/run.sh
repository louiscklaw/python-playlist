#!/usr/bin/env bash

set -ex

rm -rf ./output/*.png

pipenv run python3 src/main.py
