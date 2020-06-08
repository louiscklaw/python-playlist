#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint


def main():
    from pdf2image import convert_from_path
    pages = convert_from_path('./test_doc.pdf', 500)
    for i in range(0,len(pages)):
        pages[i].save('out.jpg%d' % i, 'JPEG')

if __name__ == '__main__':
    main()
