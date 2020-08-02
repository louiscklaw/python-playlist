#!/usr/bin/env python3
from py_imports import *

TEST_REPORT_DIRECTORY='test-reports'

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = CURR_DIR
PROJ_HOME = os.path.dirname(os.path.abspath(os.path.join(SRC_DIR,'..')))

TEST_SRC_DIR = os.path.join(SRC_DIR,'test')
TEST_META_DIR = os.path.join(CURR_DIR,'reports_meta')

META_DIRECTORY=TEST_META_DIR

REPORT_DIR = os.getenv('REPORT_DIR')
REPORT_DIRECTORY= os.getenv('REPORT_DIR')
