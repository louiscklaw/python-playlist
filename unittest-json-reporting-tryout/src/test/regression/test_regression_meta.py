#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from regression_suite1 import *
from regression_suite2 import *
from regression_suite3 import *
from regression_suite4 import *

if __name__ == '__main__':
  with open('test-reports/regression.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
