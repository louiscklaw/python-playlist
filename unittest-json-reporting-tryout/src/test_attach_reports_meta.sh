#!/usr/bin/env bash

set -ex

# pipenv sync

pipenv run python3 ./attach_reports_meta.py
