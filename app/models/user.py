from app.models.database import db
from flask_login import UserMixin
import bcrypt


class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    # client = db.relationship('Client', back_populates='user', uselist=False)
    # employee = db.relationship('Employee', back_populates='user', uselist=False)
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity':'User',
        'polymorphic_on':type
    }

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }
