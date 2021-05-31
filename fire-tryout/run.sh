#!/usr/bin/env bash

set -ex


pipenv run python3 ./hello.py
pipenv run python3 hello.py --name=David
# pipenv run python3 hello.py --help

pipenv run python3 ./calculator.py double 10
pipenv run python3 calculator.py double --number=15
