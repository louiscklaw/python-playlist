from flask import Flask, request, jsonify

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_restful import  Resource

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day"],
    storage_uri="memory://",
)

class PingResource(Resource):
    @limiter.limit("3/minute", override_defaults=True)
    def get(self):
        """Returns a greeting message"""
        return "PONG"
