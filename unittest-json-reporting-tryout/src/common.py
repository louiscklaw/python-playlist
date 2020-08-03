#!/usr/bin/env python3

from py_imports import *

def printWarning(warn):
  print(chalk.yellow(warn))

def printError(error_text):
  print(chalk.red(error_text))

def printDone():
  print(chalk.green(__file__ + ' Done'))

def parseYaml(string_in):
  return list(yaml.load_all(string_in, Loader=yaml.FullLoader))[:2]

def checkIfYamlWithFrontmatter(parse_result):
  if len(parse_result) > 1:
    frontmatter_check = parse_result[0]
    return type(frontmatter_check) == type({})
  else:
    return False

def helloCommon():
  print('helloCommon')