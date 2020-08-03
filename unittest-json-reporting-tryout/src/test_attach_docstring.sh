#!/usr/bin/env bash

set -ex

export SRC_DIR=$PWD
export PROJ_HOME=$PWD/..
export REPORT_DIR=$PROJ_HOME/test-reports

# pipenv install jsonpath_ng
# pipenv sync

pipenv run python3 ./attach_docstring.py
