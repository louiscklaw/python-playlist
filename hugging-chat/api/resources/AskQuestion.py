from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_restful import  Resource

from flask_sqlalchemy import SQLAlchemy

import hashlib

from datetime import datetime

from lib.HuggingChatProcessor import HuggingChatProcessor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day"],
    storage_uri="memory://",
)

class AskQuestionResource(Resource):
    @limiter.limit("3/minute", override_defaults=True)
    def post(self):
      print('ask_question')
      ip = request.remote_addr
      user_agent = request.headers.get("User-Agent")

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

        return jsonify({'status': 'success', 'answer': answer.text}), 200
      except KeyError as e:
        return jsonify({"error": str(e)}), 400
