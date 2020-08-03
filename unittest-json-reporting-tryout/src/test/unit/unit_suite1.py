import unittest
import random

class Test_unit_suite1(unittest.TestCase):
  """
---
Title: basic interface test
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.

### basic interface test

1. hello
1. world
1. English
1. 中文
  """

  def test_no_doc_string(self):
    print("no_doc_string")

  def test_helloworld(self):
    """
    # h1
    ## h2
    ### helloworld doc_string
    """
    print('hellworld')
