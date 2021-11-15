from app.models.database import db


class Client(db.Model):
    __tablename__ = "Client"
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    user = db.relationship('User', back_populates='client')
    address = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(16), nullable=False)
    reservations = db.relationship('Reservation',back_populates='client')
