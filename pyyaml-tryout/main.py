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


yaml_sample="""
# h1
## h2
### h3

helloworld paragraph

1. hello1
1. hello2
1. hello3
"""

yaml_with_frontmatter="""
---
Title: John
Description: helloworld
---

""" + yaml_sample


def parseYaml(string_in):
  return list(yaml.load_all(string_in, Loader=yaml.FullLoader))[:2]


def checkIfYamlWithFrontmatter(string_in):
  parse_result = parseYaml(string_in)

  if len(parse_result) > 1:
    frontmatter_check = parse_result[0]
    return type(frontmatter_check) == type({})
  else:
    return False

print(yaml_with_frontmatter)

assert True == checkIfYamlWithFrontmatter(yaml_with_frontmatter), 'test with frontmatter'
assert False == checkIfYamlWithFrontmatter(yaml_sample), 'test without frontmatter'
