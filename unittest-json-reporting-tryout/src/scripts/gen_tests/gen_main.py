#!/usr/bin/env python3

import os,sys
from pprint import pprint

list_test_type=[
  ('acceptance',1),
  ('integration',2),
  ('interface',3),
  ('regression',4),
  ('sanity',5),
  ('smoke',6),
  ('system',7),
  ('unit',8)
]

def get_gen_test_meta(test_type, test_num):
  return "python3 scripts/gen_tests/gen_test_meta.py {} {} &".format(
    test_type,
    test_num
  )

def get_gen_test(test_type, test_num):
  return "python3 scripts/gen_tests/gen_test_suite.py {} {} &".format(test_type, test_num)

template='''
# TEST_TYPE: $TEST_TYPE
rm -rf test/$TEST_TYPE/*.py

#GEN_TEST_META
$GEN_TEST_META_COMMAND

#GEN_TEST_SUITE_BODY
$GEN_TEST_SUITE_COMMAND

'''.lstrip()

list_output=[
  '#!/usr/bin/env bash\n',
  'set -ex\n',
  '\n\n'
]

for test_type, test_num in list_test_type:
  list_output.append(
    template
      .replace('$TEST_TYPE',test_type)
      .replace('$GEN_TEST_SUITE_COMMAND', '\n'.join(map(lambda x: get_gen_test(test_type,x), range(1,int(test_num)+1))) )
      .replace('$GEN_TEST_META_COMMAND', get_gen_test_meta(test_type, test_num))
    )


with open('scripts/gen_tests/gen_test_suite.sh','w') as fo:
  fo.writelines(list_output)