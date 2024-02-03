#!/usr/bin/env bash

set -ex

python -m pip install pipenv

pipenv install jupyter
pipenv install jupyter-notebook

# pipenv install pandas
# pipenv install quandl

# pipenv install seaborn
# pipenv install scikit-learn

# jupyter-notebook

