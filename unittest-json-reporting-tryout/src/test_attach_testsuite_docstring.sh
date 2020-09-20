#!/usr/bin/env bash

set -ex

export SRC_DIR=$PWD
export PROJ_HOME=$PWD/..
export REPORT_DIR=$PROJ_HOME/test-reports

# pipenv sync

pipenv run python3 ./attach_testsuite_docstring.py
