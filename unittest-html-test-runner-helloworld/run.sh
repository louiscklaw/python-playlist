#!/usr/bin/env bash

set -x

pipenv --rm

pipenv sync
pipenv run python3 main.py


cd reports
  mv TestResults*.html index.html
cd ..
