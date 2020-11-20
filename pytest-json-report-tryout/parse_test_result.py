import os,sys
from pprint import pprint
import json

in_json = ''.join(open('./.report.json','r').readlines())
result_json = json.loads(in_json)

SETUP_LBL='setup'
METADATA_LBL='metadata'

# name_result_pair = map(lambda x: {x['nodeid']: {SETUP_LBL: x['setup'], METADATA_LBL: x['metadata']}}, result_json['tests'])

# result
test_id_and_result={}
for test_value in result_json['tests']:
  test_id = test_value['metadata']['TEST_ID']
  test_result = test_value['outcome']
  test_id_and_result[test_id]=test_result

# test_id_and_result = map(lambda x: x, list(name_result_pair))
pprint(test_id_and_result)
