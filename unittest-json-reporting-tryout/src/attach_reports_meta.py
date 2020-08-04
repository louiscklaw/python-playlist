#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

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
    reports_node = reports[0]

    try_parse_yaml = parseMd(md_file_content)
    if checkMdWithFrontmatter(try_parse_yaml):
      parsed_yaml = try_parse_yaml
      parsed_yaml_frontmatter = parsed_yaml[0]
      parsed_yaml_content = parsed_yaml[1]

      for key in parsed_yaml_frontmatter.keys():
        lowered_key = key.lower()
        value = parsed_yaml_frontmatter[key]
        reports_node.value[lowered_key] = value

      reports_node.value['meta'] = parsed_yaml_content

      reports_node.value['doc_string_added_by'] = 'attach_reports_meta.py'

    writeJsonFile(json_data, json_result_filepath)

if __name__=="__main__":
  main()
  print('done')
