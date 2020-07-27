#!/usr/bin/env bash

set -x

# pipenv sync

pipenv run python3 before_test.py

pipenv run python3 main.py

pipenv run python3 after_test.py
