#!/usr/bin/env bash

set -ex

PROJ_DIR=/home/logic/_workspace/python-playlist


rsync -avzh --progress /home/logic/_workspace/github-playlist/github-build-merger-tryout/  $PROJ_DIR/github-build-merger


rsync -avzh --progress /home/logic/_workspace/github-playlist/scripts/update_main_build_chain.py  $PROJ_DIR/scripts/update_main_build_chain.py


rsync -avzh --progress /home/logic/_workspace/github-playlist/scripts/update_main_build_chain.sh  $PROJ_DIR/scripts/update_main_build_chain.sh
