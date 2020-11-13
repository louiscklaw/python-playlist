#!/usr/bin/env bash

set -x

pipenv --rm

set -ex

pipenv install requests

pipenv sync
