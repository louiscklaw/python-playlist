#!/usr/bin/env bash

set -ex

python3 scripts/update_main_build_chain.py -u
python3 scripts/update_main_build_chain.py

git add .github/workflows/master_build.yml
git add **-tryout/build.yml