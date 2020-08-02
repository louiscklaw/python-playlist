#!/usr/bin/env python3

from py_imports import *
from common import *
from config import *

def listXmlFiles():
  return filter(
    lambda x: x.find('.xml') > -1,
    subprocess.check_output('ls -1 {}'.format(REPORT_DIR).split(' ')).decode('utf-8').split('\n')
  )

def getJsonFilename(filename_in):
  return filename_in.replace('.xml','.json')

def getJsonFileFullPath(filepath_in):
  '''mechanism to get the json filename by xml filename'''

  filename = os.path.basename(filepath_in)
  return REPORT_DIR+'/'+getJsonFilename(filename)

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

def checkDirExist(dir_wanted):
  return os.path.exists(dir_wanted)

def listFileFromMetaDirectory(test_type):
  meta_directory = getRelatedMetaDirectory(test_type)

  try:
    if checkDirExist(meta_directory):
      (root, folders, files) = list(os.walk(meta_directory))[0]
    else:
      printError('the wanted directory not exist {}'.format(meta_directory))
      raise BaseException

    pass
  except Exception as e:
    printError('error during listing meta directory')
    raise e
    pass

  return root, files

def readXmlFile(xml_filepath):
  try:
    output = ''
    f_xml = open(xml_filepath,'r')
    output = f_xml.read()
    f_xml.close()

    if (output.strip() == ''):
      printError('xml file is empty')
      raise 'xml file is empty'

    return output

  except Exception as e:
    printError('error opening xml file {}'.format(xml_filepath))
    raise e

def dumpJson(json_path, data_dict):
  f_json = open(json_path,'w')
  json_data = json.dumps(data_dict)
  f_json.write(json_data)
  f_json.close()

def convertXmlToJson():
  xml_files = list(listXmlFiles())
  # pprint(xml_files)

  for xml_file in xml_files:
    # xml_file filename is expected to be something like unit.xml
    xml_path = REPORT_DIR+'/'+xml_file
    json_path = getJsonFileFullPath(xml_path)
    test_type = extractTestTypeFromXmlFilename(xml_file)


    print('opening xmlfile: {}'.format(xml_path))
    print('writing json file: {}'.format(json_path))

    try:
      (t_open, t_close) = getOpenAndClose('reports')

      raw_xml = readXmlFile(xml_path).replace('<?xml version="1.0" ?>','')

      # add <report> and </report>
      tuned_xml = t_open+raw_xml+t_close
      # print(tuned_xml)

      data_dict = xmltodict.parse(tuned_xml)


      # add some meta information from meta directory
      data_dict['reports']['meta'] = {}
      dict_path_to_meta = data_dict['reports']['meta']

      # print(checkMetaExist(test_type))
      # sys.exit()
      md_root, md_files = listFileFromMetaDirectory(test_type)
      for md_file in md_files:
        md_file_fullpath = os.path.join(md_root, md_file)
        dict_path_to_meta[getMetaName(md_file)] = getMetaContent(md_file_fullpath)

      dumpJson(json_path, data_dict)

    except Exception as e:
      printError('error found during process file {}'.format(xml_path))
      raise e


if __name__ == '__main__':
  convertXmlToJson()
  printDone()