#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from interface_suite1 import *
from interface_suite2 import *
from interface_suite3 import *

if __name__ == '__main__':
  with open('test-reports/interface.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
