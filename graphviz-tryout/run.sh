#!/usr/bin/env bash

set -ex

rm -rf **/*.pdf
rm -rf **/*.png
rm -rf **/*.gv

pipenv run python3 src/main.py
pipenv run python3 src/hello.py
pipenv run python3 src/process.py
pipenv run python3 src/fsm.py
pipenv run python3 src/cluster.py
pipenv run python3 src/er.py
pipenv run python3 src/unix.py
pipenv run python3 src/structs.py
pipenv run python3 src/structs_revisited.py
pipenv run python3 src/btree.py
pipenv run python3 src/traffic_light.py
pipenv run python3 src/fdp_clust.py
pipenv run python3 src/cluster_edge.py
pipenv run python3 src/g_c_n.py
pipenv run python3 src/angles.py
pipenv run python3 src/rank_same.py
pipenv run python3 src/test_render.py
