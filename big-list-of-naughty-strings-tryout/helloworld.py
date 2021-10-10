#!/usr/bin/env python3

import os,sys
from pprint import pprint


def helloworld():
  print('helloworld')

def getBLNS():
  fi=open('./blns.txt','r')
  lines = list(filter(lambda x: (x.find('#') == -1 and len(x.strip()) > 0), fi.readlines()))
  # notes: not a strup here
  lines = list(map(lambda x : x[:-1], lines))
  return lines

if __name__=='__main__':
  # helloworld()
  print(len(getBLNS()))
