from app import api, Dependant, db
from Schemas.DependantSchema import dependant_schema

from flask import jsonify
from marshmallow import ValidationError
from flask_restx import Resource, fields


dependantNameSpace = api.namespace('Dependants', description='eveyone depends on someone else')

depentand_model = dependantNameSpace.model('Dependant', {
    'id': fields.Integer(readonly=True, description='this is an id...'),
    'name': fields.String(required=True, description='every one has a name'),
    'collaborator_id': fields.Integer(required=True, description='id of the collaborator this person depends on')
})

@dependantNameSpace.route("/api/dependant")
class DependantController(Resource):
    @dependantNameSpace.doc('list all dependants')
    def get(self):
        dependants = Dependant.query.all()
        result = dependant_schema.dump(dependants)

        return jsonify(result)

    @dependantNameSpace.doc('add new dependant')
    @dependantNameSpace.expect(depentand_model)
    def post(self):
        try:
            data = dependant_schema.load([api.payload])[0]
        except ValidationError as err:
            return err.messages, 422

        new_dependant = Dependant(name=data['name'], collaborator_id=data['collaborator_id'])

        db.session.add(new_dependant)
        db.session.commit()
        
        result = dependant_schema.dump([new_dependant])

        return jsonify(result)  


@dependantNameSpace.route("/api/dependant/<int:id>")
@dependantNameSpace.doc(params={'id': 'GET YOUR ID!'})
class DependantIdController(Resource):
    def get(self, id):
        collaborator = Dependant.query.get(id)
        result = dependant_schema.dump([collaborator])

        return jsonify(result)