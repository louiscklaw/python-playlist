import requests
import json

url = "http://localhost:5000/helloworld"
headers = {"Content-type": "application/json"}
data = {
    "pre_prompt": f"""
    Hi, imagine you are a people named May.
    Keep your answer as simple as possible, don't be too verbose.
    """.strip(),
    "question": "what is your name ?"
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print("Response status code:", response.status_code)
print("Response text:", response.text)
