#!/usr/bin/env python3

import os,sys
from pprint import pprint
import random

test_type = sys.argv[1]
test_num = sys.argv[2]

py_import_template='''
import unittest
import random

'''.strip()

suite_template='''

class Test_$SUITE_NAME(unittest.TestCase):
  """
  # helloworld h1

  ## This is an h2 tag

  ### This is an h3 tag

  #### This is an h4 tag

  ##### This is an h5 tag

  ###### This is an h6 tag


  I think you should use an
  `<addr>` element here instead.

  First Header | Second Header
  ------------ | -------------
  Content from cell 1 | Content from cell 2
  Content in the first column | Content in the second column

  - white box test
  - test by functions
  """
'''

skipped_template='''
  @unittest.skip("demonstrating skipping")
  def test_sample_$NUMBER(self):
    self.fail("shouldn't happen")
'''

failed_template='''
  def test_sample_$NUMBER(self):
    self.fail("shouldn't happen")
'''

passed_template='''
  def test_sample_$NUMBER(self):
    self.assertTrue(True)
'''

template_list=[
  passed_template,
  failed_template,
  skipped_template
]

TEMPLATE_LIST_LEN=len(template_list)

testsuite_filename = '{}_suite{}.py'.format(test_type, test_num)
testsuite_classname = testsuite_filename.replace('.py','')

out_list = [
  py_import_template,
  suite_template.replace('$SUITE_NAME',testsuite_classname)
]

def gen_py_test_suite(test_type, file_num):
  filename= 'test/{}/{}_suite{}.py'.format(test_type, test_type, file_num)
  with open(filename,'w') as f_out:
    for i in range(0,int(random.randint(30,300))):
      random_num = random.randrange(100)

      if random_num < 66:
        # passed template
        out_list.append(template_list[0].replace('$NUMBER',str(i)))
      elif random_num >= 66 and random_num <= 90:
        # failed template
        out_list.append(template_list[1].replace('$NUMBER',str(i)))
      else:
        # skipped template
        out_list.append(template_list[2].replace('$NUMBER',str(i)))

    f_out.writelines(out_list)

    print('from {} import *'.format(testsuite_classname))

if __name__ == "__main__":
  gen_py_test_suite(test_type, test_num)
