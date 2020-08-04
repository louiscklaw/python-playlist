#!/usr/bin/env bash

set -ex

PROJ_HOME=$PWD/..

# /home/logic/_workspace/python-playlist/gatsby-test-result-page
# find /home/logic/_workspace/python-playlist/unittest-json-reporting-tryout |entr -c -s "./regen_test_result.sh"

rm -rf content/*.json

# cd ../unittest-json-reporting-tryout
#   # run unittest
#   ./run.sh
# cd ..

rsync -avzh $PROJ_HOME/unittest-json-reporting-tryout/test-reports/*.json $PROJ_HOME/gatsby-test-result-page/content/


cd src
  find . -type f -exec touch {} \;
cd ..
# yarn build


echo 'done'
