#!/usr/bin/env python3

import os,sys
from pprint import pprint

import subprocess
import xmltodict
import json

from config import *

CWD = os.path.abspath(os.getcwd())
TEST_META_DIR = os.path.join(CWD,'test_meta')

def listXmlFiles():
  return filter(
    lambda x: x.find('.xml') > -1,
    subprocess.check_output('ls -1 {}'.format(TEST_REPORT_DIRECTORY).split(' ')).decode('utf-8').split('\n')
  )

def getJsonFilename(filename_in):
  return filename_in.replace('.xml','.json')

def getJsonFileFullPath(filepath_in):
  '''mechanism to get the json filename by xml filename'''

  filename = os.path.basename(filepath_in)
  return TEST_REPORT_DIRECTORY+'/'+getJsonFilename(filename)

def getTestTypeName(xml_filename):
  "should be something link Unit/System/Smoke/Sanity/Regression/Interface/Integration/Acceptance according to xml filename"
  return os.path.basename(xml_filename).replace('.xml','')+'_test'

def getOpenAndClose(text):
  return ('<'+text+'>','</'+text+'>')

def getRelatedMetaDirectory(test_type):
  return os.path.join(TEST_META_DIR, test_type)

def checkMetaExist(test_type):
  """test_type should be something like unit/smoke/sanity...."""
  return os.path.exists(getRelatedMetaDirectory(test_type))

def extractTestTypeFromXmlFilename(xml_filename):
  return xml_filename.split('.')[0]

def getMetaName(filename):
  return filename.split('.')[0]

def getMetaContent(filename):
  return ''.join(open(filename, 'r').readlines())

def listFileFromMetaDirectory(test_type):
  (root, folders, files) = list(os.walk(getRelatedMetaDirectory(test_type)))[0]

  return root, files


def convertXmlToJson():
  xml_files = list(listXmlFiles())
  # pprint(xml_files)

  for xml_file in xml_files:
    # xml_file filename is expected to be something like unit.xml
    xml_path = TEST_REPORT_DIRECTORY+'/'+xml_file
    json_path = getJsonFileFullPath(xml_path)
    test_type = extractTestTypeFromXmlFilename(xml_file)


    print('opening xmlfile: {}'.format(xml_path))
    print('writing json file: {}'.format(json_path))

    try:
      (t_open, t_close) = getOpenAndClose('reports')

      f_xml = open(xml_path,'r')
      raw_xml = f_xml.read().replace('<?xml version="1.0" ?>','')

      tuned_xml = t_open+raw_xml+t_close
      # print(tuned_xml)

      data_dict = xmltodict.parse(tuned_xml)
      f_xml.close()

      # add some meta information from meta directory
      data_dict['reports']['meta'] = {}
      dict_path_to_meta = data_dict['reports']['meta']

      # print(checkMetaExist(test_type))
      # sys.exit()
      md_root, md_files = listFileFromMetaDirectory(test_type)
      for md_file in md_files:
        md_file_fullpath = os.path.join(md_root, md_file)
        dict_path_to_meta[getMetaName(md_file)] = getMetaContent(md_file_fullpath)
      # sys.exit()


      f_json = open(json_path,'w')
      json_data = json.dumps(data_dict)
      f_json.write(json_data)

    except Exception as e:
      print('error found during process file {}'.format(xml_path))
      raise e


if __name__ == '__main__':
  convertXmlToJson()
