from app import api, Resource, Dependant
from Schemas.DependantSchema import dependant_schema
from flask import jsonify


@api.route("/api/dependant/all")
class DependantController(Resource):
    def get(self):
        dependants = Dependant.query.all()
        result = dependant_schema.dump(dependants)

        return jsonify(result)


@api.route("/api/dependant/<int:id>")
@api.doc(params={'id': 'GET YOUR ID!'})
class DependantIdController(Resource):
    def get(self, id):
        collaborator = Dependant.query.get(id)
        result = dependant_schema.dump([collaborator])

        return jsonify(result)