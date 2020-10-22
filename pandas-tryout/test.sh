#!/usr/bin/env bash

set -ex

nodemon -w test1.py --exec "pipenv run python3 test1.py"