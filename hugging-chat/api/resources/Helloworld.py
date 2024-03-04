from flask import Flask

from flask_restful import Api, Resource

from lib.HuggingChatProcessor import HuggingChatProcessor

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        """Returns a greeting message"""
        return {"message": "Hello, world!"}
