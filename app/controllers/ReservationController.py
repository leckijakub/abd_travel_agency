# -*- coding: utf-8 -*-
from app.models.database import db
from app.models.reservation import Reservation
from flask import render_template, request, jsonify, flash, redirect
from flask_login import current_user, login_required

def index():
    reservation_id = request.args.get("id")
    # print("\n\n\n\n\n")
    # print(f"reservation id : {reservation_id}")
    # print("\n\n\n\n\n")
    if reservation_id is not None:
        reservation = current_user.reservations.filter_by(id=reservation_id).first()
        if reservation is not None:
            return render_template('reservation/details.html', reservation=reservation.serialize, name=current_user.name)
        else:
            return f"No reservation with id = {reservation_id}."
    else:
        return render_template('client/reservations.html', reservations=[reservation.serialize for reservation in Reservation.query.all()], name=current_user.name)
        # return jsonify([book.serialize for book in Book.query.all()])

def store(stat):
    reservation = Reservation(price=555, status=stat, client_id=None, employee_id = None, offer_id = None)
    db.session.add(reservation)
    db.session.commit()
    return jsonify(reservation.serialize)

@login_required
def create():
    offer_id = request.form.get('offer_id')
    if offer_id is None:
        flash(f"Offer {offer_id} does not exists!")
    else:
        reservation = Reservation(price=999, status='niezatwierdzona', client_id=current_user.id, employee_id=None, offer_id=offer_id)
        db.session.add(reservation)
        db.session.commit()
        flash("Offer reserved",'info')
    return redirect(request.referrer) # go back to the page from which request was posted

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
    flash("reservation deleted", 'warning')
    return redirect(request.referrer) # go back to the page from which request was posted
