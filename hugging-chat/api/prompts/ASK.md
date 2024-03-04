```python
from pprint import pprint
from flask import Flask, request, jsonify

from lib.HuggingChatProcessor import HuggingChatProcessor

app = Flask(__name__)

@app.route('/')
@app.route('/helloworld', methods=['GET'])
def get_hello():
  print('call received')
  my_instance = HuggingChatProcessor()
  answer = my_instance.get_answer('what is your name ?')
  print(answer)
  return answer.text

@app.route('/ask_question', methods=['POST'])
def ask_question():
  print('ask_question')
  return helloworld
```

```json
data = {
    "pre_prompt": f"""
    Hi, imagine you are a people named May.
    Keep your answer as simple as possible, don't be too verbose.""",
    "question": "what is your name ?"
}
```

i want to classify request by origin ip, log them into a sqlite db
