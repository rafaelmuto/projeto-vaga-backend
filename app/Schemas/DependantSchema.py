from marshmallow import Schema, fields


class DependantSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    collaborator_id = fields.Integer()
    createdAt = fields.DateTime()

dependant_schema = DependantSchema()
dependant_schema = DependantSchema(many=True)