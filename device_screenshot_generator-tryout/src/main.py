#!/usr/bin/env python3

import os,sys
from pprint import pprint

from PIL import Image
from subprocess import check_output
import shlex

# temp = check_output(['ls','./output'],shell=True)
# pprint(temp.decode('utf-8').split('\n'))

INPUT_DIR = '/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/input'
OUTPUT_DIR = '/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/output'
DEVICE_PHOTO_DIR = '/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/device'

png_files=[]
for root, dirs, files in os.walk(INPUT_DIR):
  for file in files:
    png_files.append(file)

pprint(list(png_files))


for png_file in png_files:
  in_filename = INPUT_DIR+'/'+png_file
  outfilename = OUTPUT_DIR+"/"+png_file

  img_01 = Image.open(in_filename)
  AppleImacPro = Image.open(DEVICE_PHOTO_DIR+'/Apple_iMac_Pro.jpg')
  new_im = Image.new('RGB', (2421,2398), (0,0,0))

  new_im.paste(AppleImacPro, (0,0))
  new_im.paste(img_01, (238,528))

  new_im.save(outfilename, "PNG")



  # AppleImacPro.show()
