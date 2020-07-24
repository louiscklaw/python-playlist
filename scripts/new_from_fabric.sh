#!/usr/bin/env bash

set -x

../scripts/new_from.sh fabric-helloworld

pipenv run python3 main.py

./run.sh
