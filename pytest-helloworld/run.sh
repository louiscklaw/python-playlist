#!/usr/bin/env bash

set -ex

pipenv run pytest --maxfail=999
