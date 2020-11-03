#coding=utf-8
#!/usr/bin/python
# 导入requests库
import requests
# 导入文件操作库

import re
import json
from pprint import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

class cls_hkex_quote_json():
  def __init__(self, hkex_json_text_result):
    self.json_raw = json.loads(hkex_json_text_result)
    self.price = self.json_raw['data']['quote']['ls']

  def helloworld(self):
    print('helloworld')

def getHKEXToken():
  print('helloworld')
  page_max = 100
  house = 'https://www.hkex.com.hk/?sc_lang=EN'
  res = requests.get(house, headers=headers)
  # print(res.text)
  r_text = res.text

  token_start_pos = r_text.find('Base64-AES-Encrypted-Token')

  # tokens are variable lenght, need to guess and re to get
  key_start_pos = token_start_pos+30
  key_end_pos = key_start_pos+100
  guess_token = r_text[key_start_pos: key_end_pos]
  out_token = re.findall('"(.+?)"', guess_token)[0]
  print(out_token)
  return out_token

def getQuote(stock_no, token):
  # url = 'https://www1.hkex.com.hk/hkexwidget/data/getequityquote?sym={}&token={}&lang=eng&qid=NULL&callback=NULL'.format(stock_no, 'evLtsLsBNAUVTPxtGqVeG7ghhF0QPfbE%2fZRmNqJFFAl1AcpYZ9AbsTC10Ghz%2fZ1R')
  url = 'https://www1.hkex.com.hk/hkexwidget/data/getequityquote?sym={}&token={}&lang=eng&qid=NULL&callback=NULL'.format(stock_no, token)

  r = requests.get(url, headers=headers)
  r_text = r.text
  json_body = re.findall('NULL\((.+?)\)', r_text)[0]

  o_json = cls_hkex_quote_json(json_body)
  o_json.helloworld()

  pprint(o_json.price)

  return ''

print(getQuote('9988',getHKEXToken()))
