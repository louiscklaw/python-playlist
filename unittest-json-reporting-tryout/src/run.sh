#!/usr/bin/env bash

set -x

export SRC_DIR=$PWD
export PROJ_HOME=$PWD/..
export REPORT_DIR=$PROJ_HOME/test-reports

pipenv sync

pipenv run python3 before_test.py

mkdir -p $REPORT_DIR

pipenv run python3 test/unit/test_unit_run.py &
pipenv run python3 test/integration/test_integration_run.py &
pipenv run python3 test/sanity/test_sanity_run.py &
pipenv run python3 test/smoke/test_smoke_run.py &
pipenv run python3 test/interface/test_interface_run.py &
pipenv run python3 test/regression/test_regression_run.py &
pipenv run python3 test/acceptance/test_acceptance_run.py &

wait

set -ex

pipenv run python3 after_test.py

pipenv run python3 ./attach_docstring.py

pipenv run python3 ./attach_testsuite_docstring.py

pipenv run python3 ./attach_reports_meta.py


# below is the code for report generation
# IDEA: it shouldn't be here, but currently no anywhere better than here.
# NOTE: related to /home/logic/_workspace/python-playlist/gatsby-test-result-page
OWD=$PWD
cd ../../gatsby-test-result-page
  ./regen_test_result.sh
cd $OWD