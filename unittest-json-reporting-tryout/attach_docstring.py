#!/usr/bin/env python3

import os,sys
from pprint import pprint

import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

sys.path.append('/home/logic/_workspace/python-playlist/unittest-json-reporting-tryout/test')

test_types = []

# from unit import *
import unit
test_types.append(('unit', unit))

# print(Test_unit_suite1.__doc__)
# print(list(filter(lambda x: x.find("test_") > -1, dir(Test_unit_suite1) )))
# print(Test_unit_suite1.test_sample_0.__doc__)

# lookinto unit

def listSuiteInsideClass(class_in):
  return filter(lambda x: x.find('Test_') > -1, dir(class_in))

def getDocString(o_in):
  NO_DOC_STRING_DEFAULT=''
  if (o_in.__doc__ == None):
    return NO_DOC_STRING_DEFAULT
  else:
    return o_in.__doc__

def extractTestcase(testtype, testsuite, testsuite_class):
  output = []
  testtype_name = testtype.__name__
  testsuite_name = testsuite.__name__
  testsuite_class_name = testsuite_class.__name__

  txt_testcases = filter(lambda x: x.find('test_') > -1, dir(testsuite_class))

  for txt_testcase in txt_testcases:
    txt_to_eval ='{}.{}.{}.{}'.format(testtype_name, testsuite_name, testsuite_class_name, txt_testcase )
    output.append((txt_to_eval, eval(txt_to_eval)))

  # return [ ('test_helloworld', unit.unit_suite1.Test_unit_suite1.test_helloworld)]
  return output

def extractFromTestSuite(testtype,testsuite):
  output = []

  # get testsuite classname
  txt_testsuite_classnames = filter(lambda x: x.find('_suite') > -1, dir(testsuite))
  testtype_name = testtype.__name__
  testsuite_name = testsuite.__name__

  for txt_testsuite_classname in txt_testsuite_classnames:
    txt_to_eval ='{}.{}.{}'.format(testtype_name, testsuite_name, txt_testsuite_classname )
    # print(txt_to_eval)
    output.append((txt_testsuite_classname,eval(txt_to_eval)))

  # return [ ('Test_unit_suite1', unit.unit_suite1.Test_unit_suite1)]
  return output

def extractFromTestType(testtype):
  output = []
  # get testsuite filename
  txt_suites = filter(lambda x: x.find('_suite') > -1, dir(testtype))
  # print(list(txt_suites))

  for txt_suite in txt_suites:
    output.append((txt_suite, eval('{}.{}'.format(testtype.__name__,txt_suite))))

  # [ ('unit_suite1', unit.unit_suite1) ]
  return output

def grepAddressAndObjFromUnittest(testtype):
  # [(
  #   'unit.unit_suite1.Test_unit_suite1.test_helloworld',
  #   'docstring'
  # )]

  output = []
  testtype_name = testtype.__name__
  testsuite_filenames = extractFromTestType(testtype)
  for txt_testsuite_filename, cls_testsuite_filename in testsuite_filenames:
    testsuite_classnames = extractFromTestSuite(testtype, cls_testsuite_filename)
    for txt, cls_testsuite in testsuite_classnames:
      for txt, cls_testcase in extractTestcase(testtype, cls_testsuite_filename, cls_testsuite):
        output.append((txt, cls_testcase))

  return output
def grepDocStrings(testtype):
  txt_obj_testcases = grepAddressAndObjFromUnittest(testtype)

  # get doc
  txt_doc_testcases = {}
  for txt, obj in txt_obj_testcases:
    # txt_doc_testcases.append((txt, obj.__doc__))
    txt_doc_testcases[txt] = obj.__doc__

  return txt_doc_testcases

def readJSONFile(filepath):
  f_json = open(filepath,'r')

  json_string = "".join(f_json.readlines())

  json_data = json.loads(json_string)
  return json_data

def appendDocString(testresult_json, clasd):
  print('helloworld')

def getTestcaseResultFromJson(test_type, json_data):
  jsonpath_expression = parse("$.reports.testsuite[*].testcase[*]")
  list_testcase = jsonpath_expression.find(json_data)

  # "@classname": "unit_suite1.Test_unit_suite1",
  # "@name": "test_helloworld",
  return list(map(lambda x: (
    '.'.join([test_type,x.value['@classname'], x.value['@name']])
    , x
    ), list_testcase))

JSON_RESULT_FILE="/home/logic/_workspace/python-playlist/unittest-json-reporting-tryout/test-reports/unit.json"


def main():
  # extract docstring from testcases py file
  test_docstring_pool =  grepDocStrings(unit)

  # load test_result json
  json_data = readJSONFile(JSON_RESULT_FILE)
  json_result_testtype = os.path.basename(JSON_RESULT_FILE).replace('.json','')
  json_result_testcase_list = getTestcaseResultFromJson(json_result_testtype,json_data)

  for test_result_path, test_result_obj in json_result_testcase_list:
    # test_result_obj.value['hello123'] = 'world123'
    if (test_result_path in test_docstring_pool.keys()):
      test_result_obj.value['doc_string'] = test_docstring_pool[test_result_path]

  f_out = open('test_output.json','w')
  json.dump(json_data, f_out, sort_keys=True, indent=2)

  # merge docstring according to test address
  # testaddress is something like `unit.unit_suite1.Test_unit_suite1.test_helloworld`

if __name__=="__main__":
  main()