#!/usr/bin/env bash

set -x

export SRC_DIR=$PWD
export PROJ_HOME=$PWD/..
export REPORT_DIR=$PROJ_HOME/test-reports

# pipenv sync

# pipenv run python3 before_test.py

# mkdir -p $REPORT_DIR

# pipenv run python3 test/unit/test_unit_run.py
pipenv run python3 test/integration/test_integration_run.py

# pipenv run python3 test/sanity/test_sanity_run.py
# pipenv run python3 test/smoke/test_smoke_run.py
# pipenv run python3 test/interface/test_interface_run.py
# pipenv run python3 test/regression/test_regression_run.py
# pipenv run python3 test/acceptance/test_acceptance_run.py

set -ex

rm -rf $REPORT_DIR/*.json

# convert xmls to jsons
pipenv run python3 after_test.py

# grep doc_string from testcases and add to json
pipenv run python3 ./attach_docstring.py

# grep doc_string from testcases and add to json(test suite)
pipenv run python3 ./attach_testsuite_docstring.py

# grep markdowns from report_meta directory and add to json
pipenv run python3 ./attach_reports_meta.py

# form a python_test_result.json
pipenv run python3 ./merge_to_one.py

# below is the code for report generation
# IDEA: it shouldn't be here, but currently no anywhere better than here.
# NOTE: related to /home/logic/_workspace/python-playlist/gatsby-test-result-page

OWD=$PWD
cd ../../gatsby-test-result-page
  ./scripts/sync_test_result.sh
cd $OWD