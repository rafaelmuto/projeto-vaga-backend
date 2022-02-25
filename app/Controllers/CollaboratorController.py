from app import api, Collaborator, db, app
from Schemas.CollaboratorSchema import collaborator_schema

from flask import jsonify
from marshmallow import ValidationError
from flask_restx import Resource, fields


collaboratorNameSpace = api.namespace('Collaborators', description='Collaborators here')

collaborator_model = collaboratorNameSpace.model('Collaborator', {
    'id': fields.Integer(readonly=True, description='this is an id...'),
    'name': fields.String(required=True, description='every one has a name'),
    'department_id': fields.Integer(required=True, description='id of the department this person works at'),
    'have_dependents': fields.Boolean(readonly=True, description='does this person have dependants?')
})

@collaboratorNameSpace.route("/api/collaborator")
class CollaboratorController(Resource):
    @collaboratorNameSpace.doc('list all collaborators')
    def get(self):
        collaborators = Collaborator.query.all()
        result = collaborator_schema.dump(collaborators)

        return jsonify(result)

    @collaboratorNameSpace.doc('add a new collaborator')
    @collaboratorNameSpace.expect(collaborator_model)
    def post(self):
        try:
            data = collaborator_schema.load([api.payload])[0]
        except ValidationError as err:
            return err.messages, 422

        new_collaborator = Collaborator(name=data['name'], department_id=data['department_id'])

        db.session.add(new_collaborator)
        db.session.commit()
        
        result = collaborator_schema.dump([new_collaborator])

        return jsonify(result)


@collaboratorNameSpace.route("/api/collaborator/<int:id>")
@collaboratorNameSpace.doc(params={'id': 'GET YOUR ID!'})
class CollaboratorIdController(Resource):
    def get(self, id):
        collaborator = Collaborator.query.get(id)

        app.logger.info(collaborator)

        result = collaborator_schema.dump([collaborator])

        app.logger.info(result)

        return jsonify(result)