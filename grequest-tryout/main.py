#!/usr/bin/env python3

import os,sys
from pprint import pprint

from fabric.api import local

import grequests
import requests

urls = [
    'http://www.example.com',
]

urls=urls*500

from datetime import datetime
rs = (grequests.get(u) for u in urls)

print(datetime.now())
for u in urls:
  requests.get(u)
print(datetime.now())
print('check point 2 done')

print(datetime.now())
grequests.map(rs)
print(datetime.now())
print('check point 1 done')

print('done')
