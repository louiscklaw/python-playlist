#!/usr/bin/env python3

import os,sys
from fabric.api import local

import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

print("r.headers['content-type']")
print(r.headers['content-type'])

print("r.encoding")
print(r.encoding)

print("r.text")
print(r.text)

print("r.json()")
print(r.json())
