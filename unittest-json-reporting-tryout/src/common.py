#!/usr/bin/env python3

from py_imports import *

def printWarning(warn):
  print(chalk.yellow(warn))

def printError(error_text):
  print(chalk.red(error_text))

def printDone():
  print(chalk.green(__file__ + ' Done'))

def parseMd(string_in):
  return frontmatter.parse(string_in)

def checkMdWithFrontmatter(obj_in):
  return len(obj_in[0].keys()) > 0

def parseYaml1(string_in):
  return list(yaml.load_all(string_in, Loader=yaml.FullLoader))[:2]

def parseYaml(string_in):
  return frontmatter.parse(string_in)


def checkIfYamlWithFrontmatter(parse_result):
  if len(parse_result) > 1:
    frontmatter_check = parse_result[0]
    return type(frontmatter_check) == type({})
  else:
    return False

def helloCommon():
  print('helloCommon')

def openJsonFile(json_filepath):
  f_json_in = open(json_filepath,'r')
  return json.load(f_json_in)

def readJSONFile(filepath):
  f_json = open(filepath,'r')

  json_string = "".join(f_json.readlines())

  json_data = json.loads(json_string)
  return json_data

def dumpJsonToFile(json_file_path, json_obj ):
  f_out = open(json_file_path,'w')
  json.dump(json_obj, f_out, sort_keys=True, indent=2)
  f_out.close()

def listJsonFileInDirectory(dir_in):
  output_json_filelist = []
  for root, dirs, files in os.walk(dir_in):
    for file in filter(lambda x: x.find('.json') > -1, files):
      output_json_filelist.append(file)
  return output_json_filelist
