from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
api = Api(app, title='ACMEVita API', description='api description goes here...', version='0.0a')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:123456@db:3306/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from Models.Department import Department
from Models.Collaborator import Collaborator
from Models.Dependant import Dependant

from Controllers.DepartmentController import *
from Controllers.CollaboratorController import *
from Controllers.DependantController import *

