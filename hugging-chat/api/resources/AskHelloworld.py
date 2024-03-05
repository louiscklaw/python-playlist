from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_restful import  Resource

from lib.HuggingChatProcessor import HuggingChatProcessor

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per day"],
    storage_uri="memory://",
)

class AskHelloworldResource(Resource):
    def get(self):
      print('call received')
      my_instance = HuggingChatProcessor()
      answer = my_instance.get_answer('what is your name ?')
      print(answer)
      return answer.text
