#!/usr/bin/env bash

set -ex

PROJ_HOME='/home/logic/_workspace/python-playlist'

rm -rf content/*.json

cd ../unittest-json-reporting-tryout
  ./run.sh
cd ..

rsync -avzh $PROJ_HOME/unittest-json-reporting-tryout/test-reports/*.json $PROJ_HOME/gatsby-test-result-page/content/

cd gatsby-test-result-page
  cd src
    find . -type f -exec touch {} \;
  cd ..
  # yarn build
cd ..

echo 'done'
