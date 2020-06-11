#!/usr/bin/env python

import os,sys
from pprint import pprint

import yaml

pprint("helloworld")

with open('./pyyaml/fruits.yml') as fi:
  fruits_list = yaml.load(fi, Loader=yaml.FullLoader)
  pprint(fruits_list)
