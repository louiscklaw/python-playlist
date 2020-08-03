#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

# import unit, integration
sys.path.append(TEST_SRC_DIR)
import unit, integration

def writeJsonFile(json_obj_in, filepath):
  f_json_out = open(filepath, 'r+')
  f_json_out.truncate(0)
  json.dump(json_obj_in, f_json_out, indent=2, sort_keys=True)


def listTestSuiteInJson(testtype, json_data):
  jsonpath_expression = parse("$.reports.testsuite[*]")
  testsuites = jsonpath_expression.find(json_data)

  testtype_name = testtype.__name__

  for testsuite in testsuites:
    testsuite_name = testsuite.value['@name'].split('-')[0]
    testsuite_obj = eval('{}.{}'.format(testtype_name,testsuite_name))

    temp = grepDocStringFromTestsuite(testsuite_obj)
    if temp == None:
      testsuite.value['doc_string'] = ''

    else:
      try:
        try_parse_yaml = parseYaml(temp)
        if checkIfYamlWithFrontmatter(try_parse_yaml):
          parsed_yaml = try_parse_yaml

          keys = parsed_yaml[0].keys()

          for key in keys:
            lowered_key = key.lower()
            value = parsed_yaml[0][key]
            testsuite.value[lowered_key] = value

          testsuite.value['doc_string'] = parsed_yaml[1]
          pass

        else:
          testsuite.value['doc_string'] = temp

      except Exception as e:
        pprint(temp)
        pprint(try_parse_yaml)
        raise e


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
