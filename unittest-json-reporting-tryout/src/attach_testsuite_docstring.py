#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

# import unit, integration
sys.path.append(TEST_SRC_DIR)
import unit, integration

def listJsonFileInDirectory(dir_in):
  output_json_filelist = []
  for root, dirs, files in os.walk(dir_in):
    for file in filter(lambda x: x.find('.json') > -1, files):
      output_json_filelist.append(file)
  return output_json_filelist


def openJsonFile(json_filepath):
  f_json_in = open(json_filepath,'r')
  return json.load(f_json_in)


def writeJsonFile(json_obj_in, filepath):
  f_json_out = open(filepath, 'r+')
  f_json_out.truncate(0)
  json.dump(json_obj_in, f_json_out, indent=2, sort_keys=True)


def parseUnittestFile(testtype):

  pass

def listTestSuiteInJson(testtype, json_data):
  jsonpath_expression = parse("$.reports.testsuite[*]")
  testsuites = jsonpath_expression.find(json_data)

  testtype_name = testtype.__name__

  for testsuite in testsuites:
    testsuite_name = testsuite.value['@name'].split('-')[0]
    testsuite_obj = eval('{}.{}'.format(testtype_name,testsuite_name))
    testsuite.value['doc_string'] = grepDocStringFromTestsuite(testsuite_obj)

  return 'hellooworld'

def grepDocStringFromTestsuite(testsuite):
  return testsuite.__doc__

def main():
  json_file_list = listJsonFileInDirectory(REPORT_DIRECTORY)
  json_file_paths = map(lambda filename: os.path.join(REPORT_DIRECTORY, filename), json_file_list)

  for json_file_path in json_file_paths:
    json_filename = os.path.basename(json_file_path)
    testtype = json_filename.replace('.json','')
    testtype_obj = eval(testtype)


    json_obj = openJsonFile(json_file_path)

    listTestSuiteInJson(testtype_obj, json_obj)

    writeJsonFile(json_obj, json_file_path)

if __name__ =="__main__":
  main()
