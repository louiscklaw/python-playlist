#!/usr/bin/env bash

set -x

rm -rf test-reports/*.xml
mkdir -p test-reports

pipenv sync

pipenv run python3 test/unit/test_unittest.py &
pipenv run python3 test/integration/test_integration.py &
pipenv run python3 test/system/test_system.py &
pipenv run python3 test/sanity/test_sanity.py &
pipenv run python3 test/smoke/test_smoke.py &
pipenv run python3 test/interface/test_interface.py &
pipenv run python3 test/regression/test_regression.py &
pipenv run python3 test/acceptance/test_acceptance.py &

wait