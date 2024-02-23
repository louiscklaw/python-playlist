import requests

url = 'https://www.carousell.com.hk/ds/interlinks/1.0/listings/1077308217?_path=%2F1.0%2Flistings%2F1077308217&ccid=1771&title=%E4%B8%89%E5%A4%A7%20Programming%20IT%20CS%20Assignment%20Coding%20%E8%A3%9C%E7%BF%92%20%E5%8A%9F%E8%AA%B2%20%20%E4%BB%A3%E5%81%9A%20%E5%90%84%E9%A1%9E%E6%9C%8D%E5%8B%99%20C++PythonJavaWebMatlab%E7%B6%B2%E9%A0%81%E9%96%'
r = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.carousell.com.hk/p/%E4%B8',
    'content-type': 'application/json',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'
})


# or r.json() if expecting JSON response
from pprint import pprint
pprint(r.json())  
