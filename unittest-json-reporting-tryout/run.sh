#!/usr/bin/env bash

set -x

PROJ_HOME='/home/logic/_workspace/python-playlist'

pipenv sync

pipenv run python3 before_test.py

pipenv run python3 test/unit/test_unittest.py &
pipenv run python3 test/integration/test_integration.py &
pipenv run python3 test/system/test_system.py &
pipenv run python3 test/sanity/test_sanity.py &
pipenv run python3 test/smoke/test_smoke.py &
pipenv run python3 test/interface/test_interface.py &
pipenv run python3 test/regression/test_regression.py &
pipenv run python3 test/acceptance/test_acceptance.py &

wait

pipenv run python3 after_test.py


rm -rf $PROJ_HOME/gatsby-test-result-page/content/*.json

rsync -avzh $PROJ_HOME/unittest-json-reporting-tryout/test-reports/*.json $PROJ_HOME/gatsby-test-result-page/content/
