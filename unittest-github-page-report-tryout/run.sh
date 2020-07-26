#!/usr/bin/env bash

set -x

rm -rf reports/*.html

# pipenv --rm
pipenv sync
pipenv run python3 main.py

mkdir -p ../docs

cp -R ./reports/*.html ../docs/index.html
