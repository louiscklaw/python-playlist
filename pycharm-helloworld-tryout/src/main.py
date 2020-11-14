#!/usr/bin/env python3
import os,sys

SRC_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(SRC_DIR+'/..')

sys.path.append(PROJ_HOME)

from src.config import *
from src.lib.helloworld import *

def funcABCDE():
  print(HELLO_CONFIG)
  print('abcde')
  funcLibHelloworld()

if __name__ == "__main__":
  funcABCDE()
