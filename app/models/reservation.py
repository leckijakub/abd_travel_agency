from app.models.database import db


class Reservation(db.Model):
    __tablename__ = "Reservation"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(32), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    client = db.relationship('Client', back_populates='reservations')
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))
    offer_id = db.Column(db.Integer, db.ForeignKey('Travel_agency_offer.id'))
    offer = db.relationship('Travel_agency_offer', back_populates='reservations')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'price': self.price,
            'status': self.status,
        }