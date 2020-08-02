#!/usr/bin/env bash
set -ex


# TEST_TYPE: acceptance
rm -rf test/acceptance/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py acceptance 1 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py acceptance 1 &

# TEST_TYPE: integration
rm -rf test/integration/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py integration 2 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py integration 1 &
python3 scripts/gen_tests/gen_test_suite.py integration 2 &

# TEST_TYPE: interface
rm -rf test/interface/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py interface 3 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py interface 1 &
python3 scripts/gen_tests/gen_test_suite.py interface 2 &
python3 scripts/gen_tests/gen_test_suite.py interface 3 &

# TEST_TYPE: regression
rm -rf test/regression/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py regression 4 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py regression 1 &
python3 scripts/gen_tests/gen_test_suite.py regression 2 &
python3 scripts/gen_tests/gen_test_suite.py regression 3 &
python3 scripts/gen_tests/gen_test_suite.py regression 4 &

# TEST_TYPE: sanity
rm -rf test/sanity/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py sanity 5 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py sanity 1 &
python3 scripts/gen_tests/gen_test_suite.py sanity 2 &
python3 scripts/gen_tests/gen_test_suite.py sanity 3 &
python3 scripts/gen_tests/gen_test_suite.py sanity 4 &
python3 scripts/gen_tests/gen_test_suite.py sanity 5 &

# TEST_TYPE: smoke
rm -rf test/smoke/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py smoke 6 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py smoke 1 &
python3 scripts/gen_tests/gen_test_suite.py smoke 2 &
python3 scripts/gen_tests/gen_test_suite.py smoke 3 &
python3 scripts/gen_tests/gen_test_suite.py smoke 4 &
python3 scripts/gen_tests/gen_test_suite.py smoke 5 &
python3 scripts/gen_tests/gen_test_suite.py smoke 6 &

# TEST_TYPE: system
rm -rf test/system/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py system 7 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py system 1 &
python3 scripts/gen_tests/gen_test_suite.py system 2 &
python3 scripts/gen_tests/gen_test_suite.py system 3 &
python3 scripts/gen_tests/gen_test_suite.py system 4 &
python3 scripts/gen_tests/gen_test_suite.py system 5 &
python3 scripts/gen_tests/gen_test_suite.py system 6 &
python3 scripts/gen_tests/gen_test_suite.py system 7 &

# TEST_TYPE: unit
rm -rf test/unit/*.py

#GEN_TEST_META
python3 scripts/gen_tests/gen_test_meta.py unit 8 &

#GEN_TEST_SUITE_BODY
python3 scripts/gen_tests/gen_test_suite.py unit 1 &
python3 scripts/gen_tests/gen_test_suite.py unit 2 &
python3 scripts/gen_tests/gen_test_suite.py unit 3 &
python3 scripts/gen_tests/gen_test_suite.py unit 4 &
python3 scripts/gen_tests/gen_test_suite.py unit 5 &
python3 scripts/gen_tests/gen_test_suite.py unit 6 &
python3 scripts/gen_tests/gen_test_suite.py unit 7 &
python3 scripts/gen_tests/gen_test_suite.py unit 8 &

