#!/usr/bin/env bash

set -ex

rsync -avzh \
  /home/logic/_workspace/python-playlist/unittest-json-reporting-tryout/test-reports/python_test_result.json \
  /home/logic/_workspace/python-playlist/gatsby-test-result-page/static/json/