from app.models.database import db


class Reservation(db.Model):
    __tablename__ = "Reservation"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(32), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
    offer_id = db.Column(db.Integer, nullable=False)
