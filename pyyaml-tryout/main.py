#!/usr/bin/env python3

import os,sys
from fabric.api import local
from pprint import pprint

import yaml

# with open('frontmatter_test.yaml') as f:
#     front_matter, content = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]

#     print('front_matter')
#     print(front_matter)

#     print('content')
#     print(content)


test="""
---
Title: John
Description: helloworld
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
"""

pprint(list(yaml.load_all(test, Loader=yaml.FullLoader))[:2])