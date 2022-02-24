import json
from app import api, Resource, Collaborator
from Schemas.CollaboratorSchema import collaborator_schema
from flask import jsonify


@api.route("/api/collaborator/all")
class CollaboratorController(Resource):
    def get(self):
        collaborators = Collaborator.query.all()
        result = collaborator_schema.dump(collaborators)

        return jsonify(result)


@api.route("/api/collaborator/<int:id>")
@api.doc(params={'id': 'GET YOUR ID!'})
class CollaboratorIdController(Resource):
    def get(self, id):
        collaborator = Collaborator.query.get(id)
        result = collaborator_schema.dump([collaborator])

        return jsonify(result)