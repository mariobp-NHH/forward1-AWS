from flask import flask
application = Flask(__name__)

@application.route('/')
def hello_world():
  return 'Hello World!'