#!/usr/bin/env python3

import os,sys
from pprint import pprint

from fabric.api import local

import grequests
import requests

urls = [
    'http://www.example.com',
]

urls=urls*3

from datetime import datetime
rs = (grequests.get(u) for u in urls)

results = grequests.map(rs)
for r in results:
  print(r.text)


print('done')
