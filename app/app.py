from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app, title='api_test', description='api description goes here...', version='0.0a')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:123456@localhost:3306/app_db'
db = SQLAlchemy(app)

from Controllers.Test import *

