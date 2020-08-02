#!/usr/bin/env python3
import os,sys
from pprint import pprint
import random
import unittest
import xmlrunner

CURR_PATH=os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_PATH)

REPORT_DIR = os.getenv('REPORT_DIR')
XML_REPORT_PATH = os.path.join(REPORT_DIR,'integration.xml')

for root, dirs, files in os.walk(CURR_PATH):
  py_files = filter(lambda filename: filename.find('.py') > -1, files)

  for py_file in py_files:

    if (py_file  in ['__init__.py']):
      # print('skipping {}'.format(py_file))
      pass

    elif (py_file.find('_run.py') > -1):
      # print('skipping {}'.format(py_file))
      pass

    else:
      # print('will import pyfile {}'.format(py_file))

      classname = py_file.replace('.py','')
      # exec('import {}'.format(classname))
      exec('from {} import *'.format(classname))


if __name__ == '__main__':
  with open(XML_REPORT_PATH, 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
