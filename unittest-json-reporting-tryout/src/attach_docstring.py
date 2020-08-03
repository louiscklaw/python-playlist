#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

sys.path.append(TEST_SRC_DIR)

# import depth=1 dir from TEST_SRC for test types
for root, dirs, files in os.walk(TEST_SRC_DIR):
  for dirname in dirs:
    # print('importing class {}'.format(dirname))
    exec('import {}'.format(dirname))


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

  # print(dir(testtype))


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


def listJsonFileInDirectory(dir_in):
  try:
    output_json_filelist = []
    for root, dirs, files in os.walk(dir_in):
      for file in filter(lambda x: x.find('.json') > -1, files):
        output_json_filelist.append(file)

    if len(output_json_filelist) < 1:
      raise 'cannot find json file to load'

    return output_json_filelist

  except Exception as e:
    printError('cannot find json file to load')
    raise e

def main():
  json_file_list = listJsonFileInDirectory(REPORT_DIRECTORY)
  json_file_paths = map(lambda filename: os.path.join(REPORT_DIRECTORY, filename), json_file_list)

  for json_file_path in json_file_paths:
    json_data = readJSONFile(json_file_path)
    json_result_testtype = os.path.basename(json_file_path).replace('.json','')
    curr_testtype = eval(json_result_testtype)

    # extract docstring from testcases py file
    test_docstring_pool =  grepDocStrings(curr_testtype)
    # test_docstring_pool =  grepDocStrings(integration)

    # load test_result json
    json_result_testcase_list = getTestcaseResultFromJson(json_result_testtype,json_data)

    for test_result_path, test_result_obj in json_result_testcase_list:
      # test_result_obj.value['hello123'] = 'world123'

      # pprint(test_docstring_pool.keys())
      # pprint(test_result_path)
      # sys.exit()

      if (test_result_path in test_docstring_pool.keys()):
        # consider 2 scenario
        # 1. this is a yaml (frontmatter + content)
        # 2. this is a markdown only (markdown content)

        temp = test_docstring_pool[test_result_path]

        if temp == None:
          test_result_obj.value['doc_string'] = ''

        else:
          # try_parse_yaml = parseYaml(temp)
          # if checkIfYamlWithFrontmatter(try_parse_yaml):
          #   parsed_yaml = try_parse_yaml
          #   test_result_obj.value['title'] = parsed_yaml[0]['Title']
          #   test_result_obj.value['doc_string'] = parsed_yaml[1]

          # else:
          #   test_result_obj.value['doc_string'] = temp


          try_parse_yaml = parseYaml(temp)
          if checkIfYamlWithFrontmatter(try_parse_yaml):
            parsed_yaml = try_parse_yaml

            keys = parsed_yaml[0].keys()

            for key in keys:
              lowered_key = key.lower()
              value = parsed_yaml[0][key]
              test_result_obj.value[lowered_key] = value

            test_result_obj.value['doc_string'] = parsed_yaml[1]
            pass

          else:
            test_result_obj.value['doc_string'] = temp


    # f_out = open(json_file_path,'w')
    # json.dump(json_data, f_out, sort_keys=True, indent=2)
    dumpJsonToFile(json_file_path, json_data)

    # merge docstring according to test address
    # testaddress is something like `unit.unit_suite1.Test_unit_suite1.test_helloworld`

if __name__=="__main__":

  main()
