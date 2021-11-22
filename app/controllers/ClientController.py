from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import db, User, Reservation, Travel_agency_offer

@login_required
def index():
    return render_template('client/index.html',name=current_user.name)


@login_required
def reservations():
    # session.query(Parent).options(lazyload(Parent.children)).all()
    # current_user.post_query = db.relationship(Reservation, lazy="dynamic")
    reservations = current_user.reservations.all()
    return render_template('client/reservations.html', reservations=[reservation.serialize for reservation in reservations], name=current_user.name)
