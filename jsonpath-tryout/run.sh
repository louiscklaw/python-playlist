#!/usr/bin/env bash

set -ex

# pipenv sync

pipenv run python3 main.py
pipenv run python3 parse_test_result_json.py
