from app.models.database import db
from app.models.reservation import Reservation
from app.models.user import User
from app.models.client import Client
from app.models.employee import Employee, employee_type
from app.models.travel_agency_offer import Travel_agency_offer
from werkzeug.security import generate_password_hash

def test_start():
    db.drop_all()
    db.create_all()
    db.session.commit()
    client1 = Client(uid="1", email="a@a", password=generate_password_hash("a", method='sha256'),name="Bob",surname="Smith", address="tu",phone_number="666 666 666")
    db.session.add(client1)
    db.session.add(Employee(uid="1", email="b@b", password=generate_password_hash("a", method='sha256'),name="Bob",surname="Smith", position=employee_type.Administrator))
    db.session.commit()

    db.session.add(Reservation(price=555, status='reservation 1', client_id=None, employee_id = None, offer_id = None))
    db.session.add(Reservation(price=123, status='reservation 2', client_id=None, employee_id = None, offer_id = None))
    db.session.add(Reservation(price=444, status='reservation 3', client_id=client1.id, employee_id = None, offer_id = None))

    reservation = db.session.query(Reservation).get(int(1))
    if reservation is not None:
        db.session.delete(reservation)


    reservation = db.session.query(Reservation).get(int(2))
    if reservation is not None:
        reservation.status = 'updated'
        reservation.price = 5
        db.session.commit()

    db.session.commit()
