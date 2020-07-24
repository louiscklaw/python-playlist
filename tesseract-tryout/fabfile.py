# /usr/bin/env python
# don't generate pyc files
import sys
sys.dont_write_bytecode = True


from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *

def init_tesseract():
    sudo('apt install -qqy tesseract-ocr')
    sudo('apt install -qqy imagemagick')

    local('pipenv')
    local('pipenv install pdf2image')
    local('pipenv install pytesseract')
