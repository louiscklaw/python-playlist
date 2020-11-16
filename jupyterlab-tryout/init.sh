#!/usr/bin/env bash

set -ex

pipenv --rm

pipenv install jupyterlab
pipenv install plotly
pipenv run jupyter labextension install jupyterlab-plotly@4.12.0
pipenv run jupyter labextension install @jupyter-widgets/jupyterlab-manager
pipenv run jupyter labextension install plotlywidget@4.12.0

pipenv install yfinance

pipenv shell
python -m ipykernel install --user --name=$(basename $VIRTUAL_ENV)

jupyter lab
