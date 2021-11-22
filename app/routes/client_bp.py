from flask import Blueprint
from app.controllers.ClientController import index, reservations
client_bp = Blueprint('client', __name__)
client_bp.route('/', methods=['GET'])(index)
client_bp.route('/reservations', methods=['GET'])(reservations)
# client_bp.route('/offers',methods=['GET'])(offers)
# book_bp.route('/create/<string:title>', methods=['POST'])(store)
# book_bp.route('/update/<int:book_id>', methods=['PATCH'])(update)
# book_bp.route('/delete/<int:book_id>', methods=['DELETE'])(delete)
