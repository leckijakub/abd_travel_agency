from app.models.database import db
import bcrypt


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    client = db.relationship('Client', back_populates='user', uselist=False)
    employee = db.relationship('Employee', back_populates='user', uselist=False)

    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }
