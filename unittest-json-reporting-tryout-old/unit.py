#!/usr/bin/env python3

import os,sys
import subprocess
from pprint import pprint

import random
import unittest
import xmlrunner
import xmltodict

from config import *

class TestSequence1(unittest.TestCase):
  def test_passed(self):
    self.assertTrue(True)

class TestSequence2(unittest.TestCase):
  def test_passed(self):
    self.assertTrue(True)

class TestSequence3(unittest.TestCase):
  def test_passed(self):
    self.assertTrue(True)

class TestSequence4(unittest.TestCase):
  def test_passed(self):
    self.assertTrue(True)

class TestSequence5(unittest.TestCase):
  def test_passed(self):
    self.assertTrue(True)

def run_test():
  unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=TEST_REPORT_DIRECTORY),
    # these make sure that some options that are not applicable
    # remain hidden from the help menu.
    failfast=False, buffer=False, catchbreak=False)

if __name__ == '__main__':
  run_test()
