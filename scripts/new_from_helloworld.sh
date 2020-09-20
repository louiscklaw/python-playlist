#!/usr/bin/env bash

set -x

../scripts/new_from.sh helloworld-tryout

pipenv run python3 main.py

./run.sh
