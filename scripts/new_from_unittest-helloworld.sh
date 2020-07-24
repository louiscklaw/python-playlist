#!/usr/bin/env bash

set -x

../scripts/new_from.sh unittest-helloworld

pipenv run python3 main.py

./run.sh
