from flask import Blueprint
from app.controllers.OfferController import index, from_reservation, manage, delete, edit, update, create


offer_bp = Blueprint('offer', __name__)
offer_bp.route('/', methods=['GET'])(index)
offer_bp.route('/from-reservation', methods=['GET'])(from_reservation)
offer_bp.route('/manage', methods=['GET'])(manage)
offer_bp.route('/delete', methods=['POST'])(delete)
offer_bp.route('/edit', methods=['GET'])(edit)
offer_bp.route('/update', methods=['POST'])(update)
offer_bp.route('/create', methods=['GET','POST'])(create)
