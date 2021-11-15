from app.models.database import db


class Travel_agency_offer(db.Model):
    __tablename__ = "Travel_agency_offer"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False)
    transport = db.Column(db.String(128), nullable=False)
    accomodation = db.Column(db.String(128), nullable=False)
    event = db.Column(db.String(128), nullable=False)
    organizer_id = db.Column(db.Integer, nullable=False)
    travel_agency_name = "My Travel Agency"
