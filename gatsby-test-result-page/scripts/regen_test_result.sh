#!/usr/bin/env bash

set -ex

rsync -avzh static/json/python_test_result.json ../unittest-json-reporting-tryout/test-reports/python_test_result.json
