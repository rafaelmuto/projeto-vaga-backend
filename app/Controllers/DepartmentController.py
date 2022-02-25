from app import api, Department, db
from Schemas.DepartmentSchema import department_schema

from flask import jsonify
from marshmallow import ValidationError
from flask_restx import Resource, fields


departmentNameSpace = api.namespace('Departments', description='Depepartments ahead!')

department_model = departmentNameSpace.model('Department', {
    'id': fields.Integer(readonly=True, description='this is an id...'),
    'name': fields.String(required=True, description='you should really name these things...')
})


@departmentNameSpace.route("/api/department")
class DepartmentController(Resource):
    @departmentNameSpace.doc('list all departments')
    def get(self):
        departments = Department.query.all()
        result = department_schema.dump(departments)

        return jsonify(result)

    @departmentNameSpace.doc('create a new department')
    @departmentNameSpace.expect(department_model)
    def post(self):
        try:
            data = department_schema.load([api.payload])[0]
        except ValidationError as err:
            return err.messages, 422

        new_department = Department(name=data['name'])

        db.session.add(new_department)
        db.session.commit()

        result = department_schema.dump([new_department])

        return jsonify(result)


@departmentNameSpace.route("/api/department/<int:id>")
@departmentNameSpace.doc(params={'id': 'GET YOUR ID!'})
class DepartmentIdController(Resource):
    def get(self, id):
        department = Department.query.get(id)
        result = department_schema.dump([department])

        return jsonify(result)
