from flask import Flask
from flask_restx import Api, Resource



app = Flask(__name__)
api = Api(app, title='api_test', description='api description goes here...', version='0.0a')


from Controllers.Test import *

