import unittest
import random

class Test_unit_suite4(unittest.TestCase):
  """
### This is suite4

new suite test
  """

  def test_sample_0(self):
    """ failed template """
    self.fail("shouldn't happen")

  def test_sample_1(self):
    """ passed template """
    self.assertTrue(True)
