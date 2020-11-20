#!/usr/bin/env bash

set -ex

export PYTHONDONTWRITEBYTECODE=1

pipenv run python -m pytest --html=output/report.html tests
