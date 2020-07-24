#!/usr/bin/env python

import os,sys
from pprint import pprint

from googlesearch import search
for url in search('louislabs', stop=20):
    print(url)

pprint("helloworld")