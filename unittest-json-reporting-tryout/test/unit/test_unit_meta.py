#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from unit_suite1 import *
from unit_suite2 import *
from unit_suite3 import *
from unit_suite4 import *
from unit_suite5 import *
from unit_suite6 import *
from unit_suite7 import *
from unit_suite8 import *

if __name__ == '__main__':
  with open('test-reports/unit.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
