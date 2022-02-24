from app import api, Resource, Department
from Schemas.DepartmentSchema import department_schema
from flask import jsonify


@api.route("/api/department")
class DepartmentController(Resource):
    def get(self):
        allDepartment = Department.query.all()
        result = department_schema.dump(allDepartment)

        return jsonify(result)