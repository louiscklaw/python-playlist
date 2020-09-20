import unittest
import random

class Test_unit_suite3(unittest.TestCase):
  """
  ### Lang test

  test the lang list
  """

  def test_sample_0(self):
    """ failed template """
    self.fail("shouldn't happen")

  def test_sample_1(self):
    """ passed template """
    self.assertTrue(True)
