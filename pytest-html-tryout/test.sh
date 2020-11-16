#!/usr/bin/env bash

set -ex

pipenv run pytest --html=dist/report.html tests/test.py
