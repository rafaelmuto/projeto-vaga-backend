from marshmallow import Schema, fields


class DepartmentSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    createdAt = fields.DateTime()

department_schema = DepartmentSchema()
department_schema = DepartmentSchema(many=True)