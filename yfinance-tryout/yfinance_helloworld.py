#!/usr/bin/env python

import os,sys
from pprint import pprint
import yfinance as yf
import json

test_stock = yf.Ticker("0388.HK")

info_json =  test_stock.info
hist = test_stock.history(period="max")


f_json = open('./info.json','w')
f_json.writelines(json.dumps(info_json))

f_history = open('./history.json','w')
print(hist)
