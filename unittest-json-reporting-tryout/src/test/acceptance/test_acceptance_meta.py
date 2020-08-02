#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from acceptance_suite1 import *

if __name__ == '__main__':
  with open('test-reports/acceptance.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
