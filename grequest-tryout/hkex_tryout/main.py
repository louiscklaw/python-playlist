#!/usr/bin/env python3

import os,sys
from pprint import pprint

import grequests

urls = [
    'https://www1.hkex.com.hk/hkexwidget/data/getequityquote?sym=9988'
]

header = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
  'Accept': 'application/json,text/javascript,*.*;q=0.01',
  'Origin': 'https://www.futunn.com',
  # 'Referer': 'https://www.futunn.com/quote/stock-info?m={0}&code={1}&type=finance_analyse'.format(market.lower(),code.upper)
}


from datetime import datetime
rs = (grequests.get(u, headers=header) for u in urls)

results = grequests.map(rs)
for r in results:
  print(r.text)


print('done')
