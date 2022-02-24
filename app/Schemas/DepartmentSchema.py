from app import app
from marshmallow import Schema, fields, ValidationError, pre_load


class DepartmentSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    createdAt = fields.DateTime()

department_schema = DepartmentSchema()
department_schema = DepartmentSchema(many=True)