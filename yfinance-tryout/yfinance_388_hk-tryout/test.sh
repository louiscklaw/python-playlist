#!/usr/bin/env bash

set -ex

pipenv run python3 dump_json.py
pipenv run python3 dump_0027.py
# pipenv run python3 yfinance_helloworld_388.py
