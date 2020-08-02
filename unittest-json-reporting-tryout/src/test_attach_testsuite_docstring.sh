#!/usr/bin/env bash

set -ex

# pipenv sync

pipenv run python3 ./attach_testsuite_docstring.py
