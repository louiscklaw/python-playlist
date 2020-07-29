#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from system_suite1 import *
from system_suite2 import *
from system_suite3 import *
from system_suite4 import *
from system_suite5 import *
from system_suite6 import *
from system_suite7 import *

if __name__ == '__main__':
  with open('test-reports/system.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
