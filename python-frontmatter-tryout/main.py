#!/usr/bin/env python3

import os,sys
from fabric.api import local
import frontmatter

md_without_frontmatter="""
# h1
## h2
### h3

helloworld paragraph

1. hello1
1. hello2
1. hello3
"""

md_with_frontmatter="""
---
Title: John
Description: helloworld
---

"""+md_without_frontmatter

parse_md_with_frontmatter = frontmatter.parse(md_with_frontmatter)
parse_md_without_frontmatter = frontmatter.parse(md_without_frontmatter)

def parseMd(string_in):
  return frontmatter.parse(string_in)

def checkMdWithFrontmatter(obj_in):
  return len(obj_in[0].keys()) > 0

print('with frontmatter')
print('-'*80)
print('frontmatter')
print(parse_md_with_frontmatter[0])

print('\n\ncontent')
print(parse_md_with_frontmatter[1])

print('\n\n\n')
print('-'*80)
print('without frontmatter')
print(parse_md_without_frontmatter)

assert True==checkMdWithFrontmatter(parseMd(md_with_frontmatter))
assert False==checkMdWithFrontmatter(parseMd(md_without_frontmatter))

print('done')
