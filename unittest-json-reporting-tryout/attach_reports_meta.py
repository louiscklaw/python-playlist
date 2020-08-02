#!/usr/bin/env python3

import os,sys
from pprint import pprint

import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

REPORT_DIRECTORY= os.path.dirname(os.path.abspath(__file__))+'/'+'test-reports'

META_DIRECTORY=os.path.dirname(
  os.path.abspath(__file__)
)+'/'+"reports_meta"

def listJsonFileInDirectory(dir_in):
  output_json_filelist = []
  for root, dirs, files in os.walk(dir_in):
    for file in filter(lambda x: x.find('.json') > -1, files):
      output_json_filelist.append(file)
  return output_json_filelist

def getMetaFilepath(result_file_in):
  return os.path.join(
    META_DIRECTORY,result_file_in.replace('.json',''),'desc.md'
  )

def openJsonFile(json_filepath):
  f_json_in = open(json_filepath,'r')
  return json.load(f_json_in)

def writeJsonFile(json_obj_in, filepath):
  f_json_out = open(filepath, 'r+')
  f_json_out.truncate(0)
  json.dump(json_obj_in, f_json_out, indent=2, sort_keys=True)

def main():
  json_result_files = listJsonFileInDirectory(REPORT_DIRECTORY)
  json_result_filepaths = map(lambda filename: os.path.join(REPORT_DIRECTORY, filename), json_result_files)

  for json_result_filepath in json_result_filepaths:
    filename = os.path.basename(json_result_filepath)
    meta_desc_filepath = getMetaFilepath(filename)
    md_file_content = ''.join(open(meta_desc_filepath, 'r').readlines())

    json_data = openJsonFile(json_result_filepath)
    jsonpath_expression = parse("$.reports")
    reports = jsonpath_expression.find(json_data)
    reports[0].value['meta'] = md_file_content

    writeJsonFile(json_data, json_result_filepath)

if __name__=="__main__":
  main()
  print('done')