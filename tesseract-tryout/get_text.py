#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
from PIL import Image
from subprocess import check_output

def main():
    print('helloworld')
    img = Image.open("./test/test_doc.jpg")
    area = (3283, 400, 3669, 725)
    cropped_img = img.crop(area)
    # cropped_img.show()
    cropped_img.save('./test/tmp.jpg',"JPEG")
    print(check_output(['tesseract','./test/tmp.jpg','stdout']))


if __name__ == '__main__':
    main()
