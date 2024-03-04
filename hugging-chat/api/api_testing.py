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

from flask_restful import Api, Resource

from lib.HuggingChatProcessor import HuggingChatProcessor

from resources.Helloworld import HelloWorldResource
from resources.Ping import PingResource

app = Flask(__name__)
app.config['RATE_LIMIT_PER_HOUR'] = 100

api = Api(app)
api.add_resource(HelloWorldResource, "/helloworld")
api.add_resource(PingResource, "/ping")

REQUEST_LOGS_DATABASE = 'request_logs.sqlite'
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class HelloWorld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    user_agent = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())

with app.app_context():
    print('create_all called')
    db.create_all()


@app.route('/')
@app.route('/helloworld', methods=['GET'])
def get_hello():
  print('call received')
  my_instance = HuggingChatProcessor()
  answer = my_instance.get_answer('what is your name ?')
  print(answer)
  return answer.text

@app.route('/ask_question', methods=['POST'])
@limiter.limit("3/minute", override_defaults=True)
def ask_question():
  print('ask_question')
  ip = request.remote_addr
  user_agent = request.headers.get("User-Agent")
  fingerprint = hashlib.md5(user_agent.encode('utf-8')).hexdigest()

  if not request.is_json:
    return jsonify({"error": "Missing JSON in request"}), 400
  
  new_message = HelloWorld(
     message='Hello World!',
     ip=ip,
     user_agent=user_agent
     )
  db.session.add(new_message)
  db.session.commit()

  data = request.get_json()
  try:
    question = data["question"]
    pre_prompt = data['pre_prompt']
    my_instance = HuggingChatProcessor()
    answer = my_instance.get_answer(question, pre_prompt)

    print(question)
    print(answer)
    
    return jsonify({'status': 'success', 'answer': answer.text}), 200
  except KeyError as e:
    return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
