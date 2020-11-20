#!/usr/bin/env bash

set -ex

export PYTHONDONTWRITEBYTECODE=1

pipenv run python -m pytest --json-report -v tests
