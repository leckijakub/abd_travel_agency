from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import db, Travel_agency_offer, Client
import uuid

@login_required
def index():
    offers = Travel_agency_offer.query.all()
    return render_template('offer/index.html', offers=[offer.serialize for offer in offers])


@login_required
def manage():
    if isinstance(current_user, Client):
        return "Insufficient priviliges!"
    offers = Travel_agency_offer.query.all()
    return render_template('offer/manage.html', offers=[offer.serialize for offer in offers])


@login_required
def delete():
    if isinstance(current_user, Client):
        return "Insufficient priviliges!"
    try:
        offer_id = request.form.get('id')
        offer = db.session.query(Travel_agency_offer).get(int(offer_id))
        if offer is not None:
            db.session.delete(offer)
            db.session.commit()
            flash("Offer deleted","warning")
        else:
            return f"Offer with id = \"{reservation_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e
    flash("Offer deleted", 'warning')
    return redirect(request.referrer) # go back to the page from which request was posted

@login_required
def from_reservation():
    reservation_id = request.args.get("id")
    if reservation_id is not None:
        reservation = current_user.reservations.filter_by(id=reservation_id).first()
        if reservation is not None:
            offer = reservation.offer
            return render_template('offer/details.html', offer=offer.serialize, name=current_user.name)
        else:
            return f"No reservation with id = {reservation_id}."
    else:
        return render_template('client/reservations.html', reservations=[reservation.serialize for reservation in Reservation.query.all()], name=current_user.name)

@login_required
def edit():
    if isinstance(current_user, Client):
            return "Insufficient priviliges!"
    offer_id = request.args.get('id')
    if offer_id is None:
        return "No offer id was provided"

    offer = db.session.query(Travel_agency_offer).get(int(offer_id))
    if offer is not None:
        return render_template('offer/edit.html', offer=offer.serialize, name=current_user.name)
    else:
            return f"No offer with id = {offer_id}."

@login_required
def update():
    if isinstance(current_user, Client):
        return "Insufficient priviliges!"
    try:
        offer_id = request.form.get('id')
        new_accommodation = request.form.get('accommodation')
        new_event = request.form.get('event')
        new_transport = request.form.get('transport')

        offer = db.session.query(Travel_agency_offer).get(int(offer_id))
        if offer is not None:
            offer.accommodation = new_accommodation
            offer.event = new_event
            offer.transport = new_transport
            db.session.commit()
        else:
            return f"Offer with id = \"{reservation_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e

    flash("Offer updated", 'info')
    return redirect(url_for('offer.manage')) # go back to the page from which request was posted

@login_required
def create():
    if isinstance(current_user, Client):
        return "Insufficient priviliges!"

    if request.method == 'GET':
        return render_template('offer/create.html', name=current_user.name)
    else:
        new_accommodation = request.form.get('accommodation')
        new_event = request.form.get('event')
        new_transport = request.form.get('transport')

        offer = Travel_agency_offer(uid=str(uuid.uuid1()), transport=new_transport, accommodation=new_accommodation, event=new_event,organizer_id=current_user.id)#db.session.query(Travel_agency_offer).get(int(offer_id))
        db.session.add(offer)
        db.session.commit()

        flash("Offer created", 'info')
        return redirect(url_for('offer.manage')) # go back to the page from which request was posted
