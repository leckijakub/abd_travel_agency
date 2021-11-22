from flask import Blueprint
from app.controllers.ReservationController import index, store, update, delete
reservation_bp = Blueprint('reservation_bp', __name__)
reservation_bp.route('/', methods=['GET'])(index)
#curl -s -X POST http://localhost:5000/reservations/create/statusR
reservation_bp.route('/create/<string:stat>', methods=['POST'])(store)
#curl -s -X PATCH http://localhost:5000/reservations/update/1?status=statusR2
reservation_bp.route('/update/<int:reservation_id>', methods=['PATCH'])(update)
reservation_bp.route('/delete/<int:reservation_id>', methods=['DELETE'])(delete)
