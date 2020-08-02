#!/usr/bin/env bash

set -ex

# pipenv install jsonpath_ng
# pipenv sync

pipenv run python3 ./attach_docstring.py
