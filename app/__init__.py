#!/usr/bin/env python
# encoding: utf-8

# DO WPROWADZANIA ZMIAN W KONTENERZE:
# docker-compose -d --build
# docker-compose up

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.book_bp import book_bp
from app.models.database import db
from app.models.user import User
from app.models.client import Client
from app.models.employee import Employee
from app.models.reservation import Reservation
from app.models.travel_agency_offer import Travel_agency_offer
# from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config.from_object("app.config.Config")
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(book_bp, url_prefix='/books/')

'''
Aby stworzyć bazę danych:
   / docker-compose exec web flask shell

A w konsoli:

    from app import db

    db.drop_all()
    db.create_all()
    db.session.commit()
'''

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

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
