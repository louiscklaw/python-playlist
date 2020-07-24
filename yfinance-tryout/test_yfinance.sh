#!/usr/bin/env bash

set -ex

cd yfinance
  pipenv run python3 runtest.py

cd ..
