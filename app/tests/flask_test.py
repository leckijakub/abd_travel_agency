from sqlalchemy.sql.expression import join
from app.models.database import db
from app.models.reservation import Reservation
from app.models.user import User
from app.models.client import Client
from app.models.employee import Employee, employee_type
from app.models.travel_agency_offer import Travel_agency_offer
from werkzeug.security import generate_password_hash
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_start():
    print(f"\n{bcolors.WARNING}WARNING: Testing database... may result in fatal errors...{bcolors.ENDC}\n")
    db.drop_all()
    db.create_all()
    db.session.commit()
    print(f"\n\n{bcolors.OKCYAN}Adding some users, an offer, and a reservation:\n{bcolors.ENDC}")

    emp1 = Employee(uid="emp1", email="b@b", password=generate_password_hash("a", method='sha256'),name="Mark",surname="Smith", position=employee_type.Administrator)
    emp2 = Employee(uid="emp2", email="b1@b", password=generate_password_hash("a", method='sha256'),name="John",surname="Constantine", position=employee_type.Animator)
    emp3 = Employee(uid="emp3", email="b2@b", password=generate_password_hash("a", method='sha256'),name="Bruce",surname="Wayne a.k.a. Batman", position=employee_type.Service_organizer)
    emp4 = Employee(uid="emp4", email="b3@b", password=generate_password_hash("a", method='sha256'),name="John",surname="Wick", position=employee_type.Reservation_empolyee)
    db.session.add_all([emp1, emp2, emp3, emp4])
    db.session.commit()

    client1 = Client(uid="1", email="a@a", password=generate_password_hash("a", method='sha256'),name="Bob", surname="Smith", address="tu",phone_number="666 666 666")
    client2 = Client(uid="2", email="a1@a", password=generate_password_hash("a", method='sha256'),name="Keanu", surname="Reeves", address="Warszawa",phone_number="420 691 337")
    client3 = Client(uid=emp3.uid, email="b2@bprivate", password=generate_password_hash("a", method='sha256'),name=emp3.name, surname=emp3.surname, address="Warszawa",phone_number="691 337 420")
    client4 = Client(uid=emp2.uid, email="b1@bprivate", password=generate_password_hash("a", method='sha256'),name=emp2.name, surname=emp2.surname, address="Warszawa",phone_number="133 742 069")
    client5 = Client(uid=emp4.uid, email="b3@bprivate", password=generate_password_hash("a", method='sha256'),name=emp4.name, surname=emp4.surname, address="Warszawa",phone_number="213 769 420")
    db.session.add_all([client1, client2, client3, client4, client5])

    offer1 = Travel_agency_offer(uid=1, transport='z buta', accommodation='pod drzewem', event='marsz',organizer_id=None)
    db.session.add(offer1)
    db.session.commit()
    db.session.add(Reservation(price=444, status='test offer', client_id=Client.query.first().id, employee_id = None, offer_id = offer1.id))
    db.session.commit()

    #json z pliku + nazwy tablic do insertowania ze zwracaniem kolumn
    jfile = open("tests/offer.json", "r")
    jobj = json.loads(jfile.read())
    offers = db.metadata.tables['Travel_agency_offer']
    reservations = db.metadata.tables['Reservation']

    from sqlalchemy import select, literal

    kobyla = reservations.insert().from_select(
        ['client_id', 'price', 'status', 'offer_id'],
        select(
            Client.id,
            literal("0"),
            literal("accepted"),
            offers.insert().values(**jobj).returning(Travel_agency_offer.id).cte('insert_query')
        ).select_from( # important
            Client
        ).join(
            Employee, Client.uid == Employee.uid
        )
    )

    print(f"\n\n{bcolors.HEADER}#################### QUERY 1 ####################\n{bcolors.ENDC}")
    print(str(kobyla)+"\n\n\n")
    db.session.execute(kobyla)
    db.session.commit()

    print(f"\n\n{bcolors.OKCYAN}Querying users and offers for new reservations:{bcolors.ENDC}\n")

    keanu = Client.query.where(Client.name == "Keanu").first()
    marsz = Travel_agency_offer.query.where(Travel_agency_offer.event == "marsz").first()

    print(f"\n\n{bcolors.OKCYAN}Adding one more reservation:{bcolors.ENDC}\n")
    db.session.add(Reservation(price=444, status='test offer', client_id=keanu.id, employee_id = None, offer_id = marsz.id))
    db.session.commit()

    print(f"\n{bcolors.OKGREEN}Querying reservations:{bcolors.ENDC}\n")
    reservations = db.session.query(Reservation).all()
    print(f"\n{bcolors.OKGREEN}Reservations result:\n{bcolors.ENDC}")
    [print(reservation.serialize) for reservation in reservations]

    print(f"\n{bcolors.OKGREEN}Querying offers:{bcolors.ENDC}\n")
    offers = db.session.query(Travel_agency_offer).all()
    print(f"\n{bcolors.OKGREEN}Offers result:\n{bcolors.ENDC}")
    [print(offer.serialize) for offer in offers]

    print(f"\n{bcolors.OKGREEN}Querying clients:{bcolors.ENDC}\n")
    clients = db.session.query(Client).all()
    print(f"\n{bcolors.OKGREEN}Clients result:\n{bcolors.ENDC}")
    [print(client.serialize) for client in clients]

    from sqlalchemy import func

    print(f"\n\n{bcolors.HEADER}#################### QUERY 2 ####################\n{bcolors.ENDC}")
    bestoffer = db.session.query(
        Travel_agency_offer
    ).select_from(
        Client
    ).filter(
        Client.address == 'Warszawa'
    ).join(
        Reservation, Client.id == Reservation.client_id
    ).join(
        Travel_agency_offer, Reservation.offer_id == Travel_agency_offer.id
    ).group_by(
        Travel_agency_offer
    ).order_by(func.count(Client.id).desc()).first()

    print(f"\n{bcolors.FAIL}Most popular offer among clients living in Warsaw: {bcolors.ENDC}" + str(bestoffer.serialize) + '\n')

    bestoffer = db.session.query(
        Client.name,
        Client.surname,
        Travel_agency_offer.accommodation,
        Reservation.id
    ).select_from(
        Client
    ).filter(
        Client.address == 'Warszawa'
    ).join(
        Reservation, Client.id == Reservation.client_id
    ).join(
        Travel_agency_offer, Reservation.offer_id == Travel_agency_offer.id
    ).all()
    
    print(f"\n{bcolors.FAIL}List of offers and clients living in Warsaw: {bcolors.ENDC}")
    [print(row) for row in bestoffer]

