from flask import Flask

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from resources.Helloworld import HelloWorldResource
from resources.Ping import PingResource
from resources.AskQuestion import AskQuestionResource
from resources.AskHelloworld import AskHelloworldResource

app = Flask(__name__)
app.config['RATE_LIMIT_PER_HOUR'] = 100

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per day"],
    storage_uri="memory://",
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    print('create_all called')
    db.create_all()

api = Api(app)
api.add_resource(HelloWorldResource, "/helloworld")
api.add_resource(PingResource, "/ping")
api.add_resource(AskHelloworldResource, "/ask_helloworld")
api.add_resource(AskQuestionResource, "/ask_question")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
