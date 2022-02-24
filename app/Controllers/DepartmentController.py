from app import api, Resource, Department
from Schemas.DepartmentSchema import department_schema
from flask import jsonify


@api.route("/api/department/all")
class DepartmentController(Resource):
    def get(self):
        departments = Department.query.all()
        result = department_schema.dump(departments)

        return jsonify(result)


@api.route("/api/department/<int:id>")
@api.doc(params={'id': 'GET YOUR ID!'})
class DepartmentIdController(Resource):
    def get(self, id):
        department = Department.query.get(id)
        result = department_schema.dump([department])

        return jsonify(result)
