from marshmallow import Schema, fields


class CollaboratorSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    department_id = fields.Integer()
    have_dependents = fields.Function(lambda Collaborator: Collaborator.hasDependants())
    createdAt = fields.DateTime()

collaborator_schema = CollaboratorSchema()
collaborator_schema = CollaboratorSchema(many=True)