#!/usr/bin/env bash

set -ex

rm -rf unittest-json-reporting-tryout/test-reports
git rm -rf unittest-json-reporting-tryout/test-reports/*.xml

git checkout unittest-json-reporting-tryout/test-reports
