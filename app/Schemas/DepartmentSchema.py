from marshmallow import Schema, fields


class DepartmentSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    createdAt = fields.DateTime(required=False)

department_schema = DepartmentSchema()
department_schema = DepartmentSchema(many=True)