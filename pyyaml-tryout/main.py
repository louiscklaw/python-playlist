#!/usr/bin/env python3

import os,sys
from fabric.api import local

import yaml

with open('frontmatter_test.yaml') as f:
    front_matter, content = list(yaml.load_all(f, Loader=yaml.FullLoader))[:2]

    print('front_matter')
    print(front_matter)

    print('content')
    print(content)