from app import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class DependantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

dependant_schema = DependantSchema()
dependant_schema = DependantSchema(many=True)