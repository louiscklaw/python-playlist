#!/usr/bin/env bash

set -ex

pipenv --rm
pipenv shell --two
pipenv install google-api-python-client google-auth-httplib2
