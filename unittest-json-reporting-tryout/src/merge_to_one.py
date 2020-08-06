#!/usr/bin/env python3
from py_imports import *
from common import *
from config import *

def main():
  python_test_result_content = {}

  pprint(JSON_REPORT_FILE_IN_DIRECTORY)

  for json_report_filepath in JSON_REPORT_FILE_FULLPATH:
    test_type = os.path.basename(json_report_filepath).replace('.json','')
    try:
      python_test_result_content[test_type] = openJsonFile(json_report_filepath)

    except Exception as e:
      print('error opening json file {}'.format(json_report_filepath))
      raise e


  createFile(PYTHON_REPORT_FILE)
  dumpJsonToFile(PYTHON_REPORT_FILE, python_test_result_content)

if __name__ == '__main__':
  main()