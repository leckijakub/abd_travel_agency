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
# from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config.from_object("app.config.Config")
# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(book_bp, url_prefix='/books/')
### MODELS

'''
Aby stworzyć bazę danych:
   / docker-compose exec web flask shell

A w konsoli:

    from app import db

    db.drop_all()
    db.create_all()
    db.session.commit()
'''

# class Autor(db.Model):
#     __tablename__ = "autor"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True, nullable=False)
#     nationality = db.Column(db.String(128), nullable=False)
#     book = relationship("Book")
'''
>>> db.session.add(Autor(name="Jan", nationality="Polish"))
>>> db.session.commit()
'''
'''
Aby stworzyć swojego użytkownika:
    db.session.add(User(email='abc@example.com'))
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
