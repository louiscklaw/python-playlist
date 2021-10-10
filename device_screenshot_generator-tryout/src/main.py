#!/usr/bin/env python3

import os,sys
from pprint import pprint

from PIL import Image
from subprocess import check_output
import shlex

# temp = check_output(['ls','./output'],shell=True)
# pprint(temp.decode('utf-8').split('\n'))

png_files=[]
for root, dirs, files in os.walk('/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/input'):
  for file in files:
    png_files.append(file)

pprint(list(png_files))


for png_file in png_files:
  in_filename = "/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/input/{}".format(png_file)
  outfilename = "/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/output/{}".format(png_file)

  img_01 = Image.open(in_filename)
  AppleImacPro = Image.open('/home/logic/_workspace/python-playlist/device_screenshot_generator-tryout/device/Apple_iMac_Pro.jpg')
  new_im = Image.new('RGB', (2421,2398), (0,0,0))

  new_im.paste(AppleImacPro, (0,0))
  new_im.paste(img_01, (238,528))

  new_im.save(outfilename, "PNG")



  # AppleImacPro.show()
