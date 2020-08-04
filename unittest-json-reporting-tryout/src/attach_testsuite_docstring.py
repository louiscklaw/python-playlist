#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

# import unit, integration
sys.path.append(TEST_SRC_DIR)
for root, dirs, files in os.walk(TEST_SRC_DIR):
  for dirname in dirs:
    exec('import {}'.format(dirname))


def writeJsonFile(json_obj_in, filepath):
  f_json_out = open(filepath, 'r+')
  f_json_out.truncate(0)
  json.dump(json_obj_in, f_json_out, indent=2, sort_keys=True)


def listTestSuiteInJson(testtype, json_data):
  ERR_CANNOT_EVAL_TESTSUITE_OBJ = "cannot evaluate testsuite object"

  jsonpath_expression = parse("$.reports.testsuite[*]")
  testsuites = jsonpath_expression.find(json_data)

  testtype_name = testtype.__name__

  for testsuite in testsuites:
    testsuite_name = testsuite.value['@name'].split('-')[0]

    try:
      testsuite_obj = eval('{}.{}'.format(testtype_name,testsuite_name))

    except Exception as e:
      pprint(testtype_name)
      pprint(testsuite_name)
      raise ERR_CANNOT_EVAL_TESTSUITE_OBJ


    temp = grepDocStringFromTestsuite(testsuite_obj)

    testsuite.value['doc_string'] = ''
    testsuite.value['doc_string_added_by'] = 'attach_testsuite_docstring.py'

    if temp == None:
      pass
    else:
      try:
        try_parse_yaml = parseMd(temp)
        parsed_yaml_frontmatter = try_parse_yaml[0]
        parsed_yaml_content = try_parse_yaml[1]

        if checkMdWithFrontmatter(try_parse_yaml):

          for key in parsed_yaml_frontmatter.keys():
            lowered_key = key.lower()
            value = parsed_yaml_frontmatter[key]
            testsuite.value[lowered_key] = value

          testsuite.value['doc_string'] = parsed_yaml_content

        else:
          testsuite.value['doc_string'] = parsed_yaml_content

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
