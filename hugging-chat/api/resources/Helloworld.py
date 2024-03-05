from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        """Returns a greeting message"""
        return {"message": "Get Hello, world!"}
    
    def post(self):
        """Returns a greeting message"""
        return {"message": "Post Hello, world!"}
