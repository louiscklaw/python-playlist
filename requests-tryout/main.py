#!/usr/bin/env python3

import os,sys
from pprint import pprint

import requests


MANAGE_TOKEN='c670dbb4543e8eab16cb1ce7510f145d94a84f419050e666bb914b083bdc6448ffd5d8551d93eebc11f9d46842e440d43459bc26b9ef7374b9ac1a6566ab0dc0'


url = 'http://httpbin.org/cookies'
cookies = dict(manage_token=MANAGE_TOKEN)
r = requests.get(url, cookies=cookies)

print(r.status_code)
print(r.text)
