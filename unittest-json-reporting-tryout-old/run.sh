#!/usr/bin/env bash

set -x

PROJ_HOME='/home/logic/_workspace/python-playlist'

# pipenv sync

pipenv run python3 before_test.py

pipenv run python3 -m unittest discover
# pipenv run python3 main.py &
# pipenv run python3 unit.py &
# pipenv run python3 integration.py &
# pipenv run python3 system.py &
# pipenv run python3 sanity.py &
# pipenv run python3 smoke.py &
# pipenv run python3 interface.py &
# pipenv run python3 regression.py &

# wait

pipenv run python3 after_test.py


rm -rf $PROJ_HOME/gatsby-test-result-page/content/TEST*.json

rsync -avzh $PROJ_HOME/unittest-json-reporting-tryout/test-reports/TEST*.json $PROJ_HOME/gatsby-test-result-page/content/
