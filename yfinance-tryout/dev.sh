#!/usr/bin/env bash

set -ex

nodemon -w . -e * --exec "pipenv run python3 helloworld.py"
