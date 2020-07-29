#!/usr/bin/env bash

set -x

PROJ_HOME='/home/logic/_workspace/python-playlist'

pipenv sync

pipenv run python3 before_test.py

pipenv run python3 test/unit/test_unit_meta.py &
pipenv run python3 test/integration/test_integration_meta.py &
pipenv run python3 test/system/test_system_meta.py &
pipenv run python3 test/sanity/test_sanity_meta.py &
pipenv run python3 test/smoke/test_smoke_meta.py &
pipenv run python3 test/interface/test_interface_meta.py &
pipenv run python3 test/regression/test_regression_meta.py &
pipenv run python3 test/acceptance/test_acceptance_meta.py &

wait

pipenv run python3 after_test.py
