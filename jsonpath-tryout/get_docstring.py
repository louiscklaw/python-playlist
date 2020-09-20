#!/usr/bin/env python3

import os,sys
from pprint import pprint

sys.path.append(os.getcwd())
# sys.path.append(os.getcwd()+'/test')

from unit import *

def helloworld():
  print('helloworld')

helloworld()
print(dir(globals))
