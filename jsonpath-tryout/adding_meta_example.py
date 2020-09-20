#!/usr/bin/env python3

import os,sys
import json
from pprint import pprint

from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

f_json = open('./unit.json','r')
json_string = "".join(f_json.readlines())
json_data = json.loads(json_string)

def filterTestcaseJSON(json_data, testcase_class, testcase_name):
  test_filter = '''
  $.reports
      .testsuite[*]
        .testcase[?( @.@classname == "{}" )]
  '''.format(testcase_class).replace('\n','').strip()

  js_exp_filter_time = parse(test_filter)
  match_filter_time = js_exp_filter_time.find(json_data)

  test_python_filter = filter(lambda x: x.value['@name'] == testcase_name, match_filter_time)

  return list(test_python_filter)[0]

def addMetaToTestcase(testcase_node, field_name_value):
  field_name, field_value = field_name_value
  testcase_node.value[field_name] = field_value

addMetaToTestcase(filterTestcaseJSON( json_data, 'unit_suite1.Test_unit_suite1', 'test_sample_1'), ('meta', 'helloworld'))

fw_json = open('./updated_unit.json','w')
fw_json.write(json.dumps(json_data, indent=2, sort_keys=True))
