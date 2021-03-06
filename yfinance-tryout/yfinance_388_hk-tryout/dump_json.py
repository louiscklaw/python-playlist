#!/usr/bin/env python

import os,sys
from pprint import pprint
import yfinance as yf
import json

def getMA(df, samples=10):
  df['SMA_'+str(samples)] = df.loc[:,'Close'].rolling(window=samples).mean()

test_stock = yf.Ticker("0027.HK")

info_json =  test_stock.info
hist = test_stock.history(period="max")

for i in [10,20,50,100,150]:
  getMA(hist,i)

hist.to_json('./0027_dump.json')

print(hist.iloc[-1:]['Open'])

# print(hist.tail())
