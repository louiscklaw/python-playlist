#!/usr/bin/env bash

set -ex

rm -rf reports/*.html

pipenv sync
pipenv run python3 main.py


cd reports
  mv TestResults*.html index.html
cd ..

push-dir --dir=reports --branch=gh-pages
