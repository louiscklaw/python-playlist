#!/usr/bin/env python3

import os,sys
from pprint import pprint

CURR_PATH=os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_PATH)

for root, dirs, files in os.walk(CURR_PATH):
  py_files = filter(lambda filename: filename.find('.py') > -1, files)

  for py_file in py_files:

    if (py_file  in ['__init__.py']):
      print('skipping {}'.format(py_file))

    elif (py_file.find('_run.py') > -1):
      print('skipping {}'.format(py_file))

    else:
      print('will import pyfile {}'.format(py_file))
      classname = py_file.replace('.py','')
      exec('import {}'.format(classname))
