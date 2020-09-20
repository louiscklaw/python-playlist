#!/usr/bin/env python3

import os,sys
from pprint import pprint
import random

test_type = sys.argv[1]
test_num = sys.argv[2] # final number of the test suite

test_template='''
#!/usr/bin/env python3

import random
import unittest
import xmlrunner

$IMPORTS

if __name__ == '__main__':
  with open('test-reports/$TEST_TYPE.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
'''.lstrip()

import_template='''from $TEST_TYPE_suite$TEST_NUM import *'''

def get_import_tempalte(test_type, test_num):
  output = import_template
  return output.replace('$IMPORTS', import_template).replace('$TEST_TYPE', test_type).replace('$TEST_NUM', test_num)

list_output = [
  test_template
    .replace('$IMPORTS', '\n'.join(map(lambda x: get_import_tempalte(test_type, str(x)), range(1,int(test_num)+1))))
    .replace('$TEST_TYPE',test_type )
]

with open('test/{}/test_{}_meta.py'.format(test_type,test_type),'w') as f_py:
  f_py.writelines(list_output)