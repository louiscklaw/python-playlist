#!/usr/bin/env bash

set -ex

firefox http://localhost:8082 &

pipenv run luigid
