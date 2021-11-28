from app.models.database import db

class Travel_agency_offer(db.Model):
    __tablename__ = "Travel_agency_offer"
    travel_agency_name = "My Travel Agency"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False, autoincrement=True)
    transport = db.Column(db.String(128), nullable=False)
    accommodation = db.Column(db.String(128), nullable=False)
    event = db.Column(db.String(128), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))
    reservations = db.relationship("Reservation", back_populates='offer', cascade="all, delete")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'transport': self.transport,
            'accommodation': self.accommodation,
            'event': self.event
        }
