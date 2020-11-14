#!/usr/bin/env bash

set -ex

pipenv run pytest -q tests/main.py
