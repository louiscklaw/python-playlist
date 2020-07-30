#!/usr/bin/env python3

import os,sys
from pprint import pprint
import ast

class helloworld_class():
  """helloworld class docstring"""

  def my_func():
      """My docstring is both funny and informative"""
      pass

print(helloworld_class.__doc__)
print(helloworld_class.my_func.__doc__)
