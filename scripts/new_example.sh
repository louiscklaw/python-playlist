#!/usr/bin/env bash

cp ../scripts/main.py ./main.py
cp ../scripts/Pipfile ./Pipfile

touch Pipfile

# pipenv shell --three

pipenv run python3 -V

find . |entr -c -s "pipenv run python3 main.py"

# done
