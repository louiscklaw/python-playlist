#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from sanity_suite1 import *
from sanity_suite2 import *
from sanity_suite3 import *
from sanity_suite4 import *
from sanity_suite5 import *

if __name__ == '__main__':
  with open('test-reports/sanity.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
