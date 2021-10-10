import os,sys
from pprint import pprint

import requests

r = requests.post('http://httpbin.org/post', json={"key": "value"})
pprint(r.status_code)
'200'

pprint(r.json()['headers'])
'''
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx'},
 'json': {'key': 'value'},
 'origin': 'x.x.x.x',
 'url': 'http://httpbin.org/post'}
'''
