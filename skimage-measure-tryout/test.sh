#!/usr/bin/env bash

set -ex

echo "compare same image"
pipenv run python3 main.py -f helloworld1.png -s helloworld1.png

echo "compare different image"
pipenv run python3 main.py -f helloworld1.png -s helloworld2.png
