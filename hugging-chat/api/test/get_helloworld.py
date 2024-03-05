import requests
import json

url = "http://localhost:5000/helloworld"
headers = {"Content-type": "application/json"}

response = requests.get(url, headers=headers)
print("Response status code:", response.status_code)
print("Response text:", response.text)
