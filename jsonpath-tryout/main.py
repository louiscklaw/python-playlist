#!/usr/bin/env python3

import os,sys
import json

from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

from pprint import pprint


f_json = open('./store.json','r')

json_string = "".join(f_json.readlines())

json_data = json.loads(json_string)


jsonpath_expression = parse("$.store.book[?(@.price < 10)]")

match = jsonpath_expression.find(json_data)

# print(match)
print("id value is")
pprint(match[0].value['title'])

match[0].value['hello'] = 'helloworld'
pprint(match[0].value['hello'])

fw_json = open('./store_writing_helloworld.json','w')
fw_json.writelines(json.dumps(json_data))
