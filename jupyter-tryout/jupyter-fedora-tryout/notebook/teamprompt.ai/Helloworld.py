import os, sys
import requests
import json

def SendQuestion(BEARER, question):
  url = 'https://gptapi.apoidea.ai/v1/conversation/conversations'
  headers = {
      'authority': 'gptapi.apoidea.ai',
      'accept': 'text/event-stream',
      'accept-language': 'en-US,en;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7,zh;q=0.6',
      'authorization': BEARER,
      'cache-control': 'no-cache',
      'content-type': 'application/json',
      'origin': 'https://teamprompt.ai',
      'pragma': 'no-cache',
      'referer': 'https://teamprompt.ai/',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Linux"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
  }
  
  data = {
    "prompt": question,
    "stream": False
  }

  response = requests.post(url, headers=headers, json=data)
  return json.loads(response.text)
