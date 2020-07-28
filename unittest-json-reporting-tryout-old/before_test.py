#!/usr/bin/env python3

import os,sys
import subprocess
from pprint import pprint

import random
import unittest
import xmlrunner
import xmltodict

from config import *


def cleanReportDirectory():
  os.system('rm -rf {}/*.xml'.format(TEST_REPORT_DIRECTORY))
  os.system('rm -rf {}/*.json'.format(TEST_REPORT_DIRECTORY))

def before_test():
  cleanReportDirectory()


if __name__ == '__main__':
  before_test()
