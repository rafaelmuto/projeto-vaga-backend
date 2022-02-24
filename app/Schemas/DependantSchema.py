from marshmallow import Schema, fields


class DependantSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    createdAt = fields.DateTime()

dependant_schema = DependantSchema()
dependant_schema = DependantSchema(many=True)