#!/usr/bin/env python

import os,sys
from pprint import pprint
import yfinance as yf
import json

def getMA(df, samples=10):
  df['SMA_'+str(samples)] = df.loc[:,'Close'].rolling(window=samples).mean()

test_stock = yf.Ticker("0027.HK")

hist = test_stock.history(period="max")

hist.to_json('./0027_dump.json')
