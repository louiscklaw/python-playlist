#!/usr/bin/env python

import os,sys
from pprint import pprint
import yfinance as yf
import json
import pandas as pd

def getMA(df, samples=10):
  df['SMA_'+str(samples)] = df.loc[:,'Close'].rolling(window=samples).mean()

hist = pd.read_json('./388_dump.json')

for i in [10,20,50,100,150]:
  getMA(hist,i)
