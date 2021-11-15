from app.models.database import db


class Client(db.Model):
    __tablename__ = "Client"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(16), nullable=False)
