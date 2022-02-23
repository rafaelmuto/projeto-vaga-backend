from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
api = Api(app, title='api_test', description='api description goes here...', version='0.0a')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:123456@db:3306/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from Models.Departament import Departament

from Controllers.Test import *

