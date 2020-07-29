#!/usr/bin/env bash

set -ex

PROJ_HOME=gatsby-test-result-page

rm -rf content/*.json

cd ../unittest-json-reporting-tryout
  ./run.sh
cd ..

cd gatsby-test-result-page

echo 'done'
