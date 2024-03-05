from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from _poc.nocodb.create_ask_record import create_ask_record

# Define the NoCodeDB configuration
host = '192.168.10.61'
port = 8081
api_key = 'TdryW6UByeXUqjZfa0AdRb3GIeebj8IwltDYmAUu'
table_id = 'm90fau872vtveh6'
api_endpoint = f'http://{host}:{port}/api/v2'

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        """Returns a greeting message"""
        response = { "message": "Get Hello, world!" }
        return jsonify(response)
    
    def post(self):
        """Returns a greeting message"""

        ips = []
        if hasattr(request, 'access_route'):
            # For Flask < 2.0 compatibility
            ips += request.access_route
            
        ips.append(request.remote_addr)
        ip = ', '.join(ips)
        user_agent = request.user_agent.string
        json_body = request.get_json()
        question = json_body['question']
        pre_prompt = json_body['pre_prompt']

        create_ask_record(ip,user_agent,pre_prompt,question,'a', json_body)
        return jsonify({"message": "Post Hello, world!"})
