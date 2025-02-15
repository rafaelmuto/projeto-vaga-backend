from app import db
from datetime import datetime

class Collaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    dependants = db.relationship('Dependant', backref='collaborator')
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def hasDependants(self):
        return len(self.dependants) > 0

    def __repr__(self) -> str:
        return f"id: {self.id}, Name : {self.name}, Department: {self.department_id}, createdAt: {self.createdAt}"