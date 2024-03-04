from pprint import pprint
from flask import Flask, request, jsonify
import sqlite3
import time

import hashlib
from datetime import timedelta
from datetime import datetime

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

from lib.HuggingChatProcessor import HuggingChatProcessor

app = Flask(__name__)

DATABASE = 'request_logs.sqlite'
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"

@app.route('/')
@app.route('/helloworld', methods=['GET'])
def get_hello():
  print('call received')
  my_instance = HuggingChatProcessor()
  answer = my_instance.get_answer('what is your name ?')
  print(answer)
  return answer.text

@app.route('/ask_question1', methods=['POST'])
def ask_question1():
  print('ask_question')

  if not request.is_json:
    return jsonify({"error": "Missing JSON in request"}), 400
  
  data = request.get_json()
  try:
    question = data["question"]
    pre_prompt = data['pre_prompt']
    my_instance = HuggingChatProcessor()
    answer = my_instance.get_answer(question, pre_prompt)

    print(question)
    print(answer)
    
    return jsonify({"answer":answer.text      }), 200
  except KeyError as e:
    return jsonify({"error": str(e)}), 400

@app.route('/ask_question', methods=['POST'])
@limiter.limit("1/minute", override_defaults=True)
def ask_question():
  print('ask_question')
  ip = request.remote_addr
  user_agent = request.headers.get("User-Agent")
  fingerprint = hashlib.md5(user_agent.encode('utf-8')).hexdigest()

  if not request.is_json:
    return jsonify({"error": "Missing JSON in request"}), 400
  
  connection = None

  data = request.get_json()
  try:
    question = data["question"]
    pre_prompt = data['pre_prompt']
    my_instance = HuggingChatProcessor()
    answer = my_instance.get_answer(question, pre_prompt)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    # cursor.execute('INSERT INTO request_logs VALUES (?,?)', (int(time.time()), str(answer.text)))
    connection.commit()

    print(question)
    print(answer)
    
    return jsonify({'status': 'success', 'answer': answer.text}), 200
  except KeyError as e:
    return jsonify({"error": str(e)}), 400

@app.route('/xxx', methods=['POST'])
def post_hello():
    print('ask_question')

    connection = None
    try:
        data = request.get_json()
        question = data["question"]
        pre_prompt = data['pre_prompt']
        my_instance = HuggingChatProcessor()
        answer = my_instance.get_answer(question, pre_prompt)

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO request_logs VALUES (?,?)', (int(time.time()), str(answer.text)))
        connection.commit()

        return jsonify({'status': 'success', 'response': answer.text}), 200
    except Exception as e:
        error_msg = f"Error occurred while connecting to DB: {str(e)}"
        print(error_msg)
        raise e
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
