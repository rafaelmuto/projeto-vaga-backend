from app import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class CollaboratorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

collaborator_schema = CollaboratorSchema()
collaborator_schema = CollaboratorSchema(many=True)