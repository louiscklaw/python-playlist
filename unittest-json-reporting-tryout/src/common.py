#!/usr/bin/env python3

from py_imports import *

def printWarning(warn):
  print(chalk.yellow(warn))

def printError(error_text):
  print(chalk.red(error_text))

def printDone():
  print(chalk.green(__file__ + ' Done'))
