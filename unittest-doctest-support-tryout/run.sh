#!/usr/bin/env bash

set -x

rm -rf test-reports/*.xml
mkdir -p test-reports

pipenv sync

pipenv run python3 test/unit/test_unit.py
