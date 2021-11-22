from app.models.database import db
from app.models.user import User


class Client(User):
    __tablename__ = "Client"
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    # user = db.relationship('User', back_populates='client')
    address = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(16), nullable=False)
    reservations = db.relationship('Reservation',back_populates='client',lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity':'Client',
    }
