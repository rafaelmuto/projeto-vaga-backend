from marshmallow import Schema, fields


class CollaboratorSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    createdAt = fields.DateTime()

collaborator_schema = CollaboratorSchema()
collaborator_schema = CollaboratorSchema(many=True)