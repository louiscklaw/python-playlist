#!/usr/bin/env bash

set -ex

pipenv install jupyterlab
pipenv run jupyter labextension install jupyterlab-plotly@4.12.0
pipenv run jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.12.0

pipenv run jupyter lab
