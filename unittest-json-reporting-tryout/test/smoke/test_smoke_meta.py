#!/usr/bin/env python3

import random
import unittest
import xmlrunner

from smoke_suite1 import *
from smoke_suite2 import *
from smoke_suite3 import *
from smoke_suite4 import *
from smoke_suite5 import *
from smoke_suite6 import *

if __name__ == '__main__':
  with open('test-reports/smoke.xml', 'w') as output:
    unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
