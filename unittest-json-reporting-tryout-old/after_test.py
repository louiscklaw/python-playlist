#!/usr/bin/env python3

import os,sys
from pprint import pprint

import subprocess
import xmltodict
import json

from config import *

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

def convertXmlToJson():
  xml_files = list(listXmlFiles())
  pprint(xml_files)

  for xml_file in xml_files:
    xml_path = TEST_REPORT_DIRECTORY+'/'+xml_file
    json_path = getJsonFileFullPath(xml_path)

    print('opening xmlfile: {}'.format(xml_path))
    print('writing json file: {}'.format(json_path))

    try:
      f_xml = open(xml_path,'r')
      data_dict = xmltodict.parse(f_xml.read())
      f_xml.close()

      f_json = open(json_path,'w')
      json_data = json.dumps(data_dict)
      f_json.write(json_data)

    except Exception as e:
      print('error found during process file {}'.format(xml_path))
      raise e


if __name__ == '__main__':
  convertXmlToJson()
