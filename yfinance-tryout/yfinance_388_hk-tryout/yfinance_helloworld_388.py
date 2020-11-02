#!/usr/bin/env python

import os,sys
from pprint import pprint
import yfinance as yf
import json

def getMA(df, samples=10):
  df['SMA_'+str(samples)] = df.loc[:,'Close'].rolling(window=samples).mean()

test_stock = yf.Ticker("0388.HK")

info_json =  test_stock.info
hist = test_stock.history(period="max")

for i in [10,20,50,100,150]:
  getMA(hist,i)


print(hist.iloc[-10:,:])

print(hist.tail())
