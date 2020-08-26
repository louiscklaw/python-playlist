#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
import shlex

import subprocess

command = shlex.split('hostname')

test = subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)

print(test.stdout)