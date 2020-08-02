#!/usr/bin/env python3

import os,sys
import json
from pprint import pprint

from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


f_json = open('./test_result.json','r')

json_string = "".join(f_json.readlines())

json_data = json.loads(json_string)


jsonpath_expression = parse("$.reports.testsuite[*].testcase[*]")

match = jsonpath_expression.find(json_data)
matched_in_json = match

for test_result in matched_in_json:
  test_result_value = test_result.value
  classname = test_result_value['@classname']
  testname = test_result_value['@name']
  test_result_value['hello123'] = 'world123'
  pprint('{}.{}'.format(classname, testname))

  print(json_data)
  break

  # print(matched_in_json)
  # class_name = matched_in_json

  # print("id value is")
  # print(class_name)

  # pprint(len(matched_in_json))

# match[0].value['hello'] = 'helloworld'
# pprint(match[0].value['hello'])

# fw_json = open('./store_writing_helloworld.json','w')
# fw_json.writelines(json.dumps(json_data))
