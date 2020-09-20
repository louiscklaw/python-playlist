#!/usr/bin/env bash

set -ex

python3 scripts/gen_tests/gen_main.py

chmod +x scripts/gen_tests/gen_test_suite.sh

scripts/gen_tests/gen_test_suite.sh
