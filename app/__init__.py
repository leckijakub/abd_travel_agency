#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.routes.reservation_bp import reservation_bp
from app.routes.main_bp import main_bp
from app.routes.client_bp import client_bp
from app.routes.offer_bp import offer_bp
from app.models import *
# from app.models.database import db
# from app.models.user import User
# from app.models.client import Client
# from app.models.employee import Employee
# from app.models.reservation import Reservation
# from app.models.travel_agency_offer import Travel_agency_offer
from app.tests.flask_test import test_start
# from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config.from_object("app.config.Config")
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(main_bp)
app.register_blueprint(reservation_bp, url_prefix='/reservations/')
app.register_blueprint(client_bp, url_prefix='/client/')
app.register_blueprint(offer_bp, url_prefix='/offers/')

login_manager = LoginManager(app)
login_manager.login_view = 'main.login'

'''
Aby stworzyć bazę danych:
   / docker-compose exec web flask shell

A w konsoli:

    from app import db

    db.drop_all()
    db.create_all()
    db.session.commit()
Dodawanie rezerwacji
    db.session.add(Reservation(price=555, status='reservation status', client_id=None, employee_id = None, offer_id = None))
'''

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

### CONTROLLERS

@app.route('/', methods=['GET'])
def index():
   return jsonify(hello="world from root")

@app.route('/clear',methods=['GET'])
def clearall():
   db.drop_all()
   db.create_all()
   db.session.commit()
   return "DATABASE CLEARED\n"

@app.route('/test',methods=['GET'])
def testall():
   test_start()
   return "DATABASE TESTED\n"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
