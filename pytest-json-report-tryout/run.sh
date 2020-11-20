#!/usr/bin/env bash

set -x

export PYTHONDONTWRITEBYTECODE=1

pipenv run python -m pytest --json-report -v tests

python3 ./parse_test_result.py
