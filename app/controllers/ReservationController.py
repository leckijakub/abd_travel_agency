# -*- coding: utf-8 -*-
from app.models.database import db
from app.models.reservation import Reservation
from flask import render_template, request, jsonify

def index():
    reservation_id = request.args.get('id')
    if reservation_id is not None:
        reservation = db.session.query(Reservation).get(int(reservation_id))
        if reservation is not None:
            return jsonify(Reservation.query.get(int(reservation_id)).serialize)
        else:
            return f"No reservation with id = {reservation_id}."
    else:
        return render_template('reservation/reservations.html', reservations=[reservation.serialize for reservation in Reservation.query.all()])
        # return jsonify([book.serialize for book in Book.query.all()])

def store(stat):
    reservation = Reservation(price=555, status=stat, client_id=None, employee_id = None, offer_id = None)
    db.session.add(reservation)
    db.session.commit()
    return jsonify(reservation.serialize)

def update(reservation_id):
    new_status = request.args.get('status')
    new_price = request.args.get('price')
    try:
        reservation = db.session.query(Reservation).get(int(reservation_id))
        if reservation is not None:
            if new_status != None:
                reservation.status = new_status
            if new_price != None:
                reservation.price = new_price
            db.session.commit()
        else:
            return f"reservation with id = \"{reservation_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e
    return "reservation updated"

def delete(reservation_id):
    try:
        reservation = db.session.query(Reservation).get(int(reservation_id))
        if reservation is not None:
            db.session.delete(reservation)
            db.session.commit()
        else:
            return f"reservation with id = \"{reservation_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e
    return "reservation deleted"    
