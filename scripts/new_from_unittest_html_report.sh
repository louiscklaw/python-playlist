#!/usr/bin/env bash

set -x

../scripts/new_from.sh unittest-html-test-runner-helloworld

pipenv run python3 main.py

./run.sh
