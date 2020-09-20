#!/usr/bin/env bash

set -ex

pipenv shell --three exit 0

pip install notebook