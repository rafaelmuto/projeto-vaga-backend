from app import db
from datetime import datetime

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    colaborators = db.relationship('Collaborator', backref='department', lazy=True)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"id: {self.id}, Name : {self.name}, createdAt: {self.createdAt}"