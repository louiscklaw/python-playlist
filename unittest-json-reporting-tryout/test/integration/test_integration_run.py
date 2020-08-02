#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from integration_suite1 import *
# from integration_suite2 import *

if __name__ == '__main__':
  with open('test-reports/integration.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
