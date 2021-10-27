from flask import Blueprint
from app.controllers.BookController import index, store, update, delete
book_bp = Blueprint('user_bp', __name__)
book_bp.route('/', methods=['GET'])(index)
book_bp.route('/create/<string:title>', methods=['POST'])(store)
book_bp.route('/update/<int:book_id>', methods=['PATCH'])(update)
book_bp.route('/delete/<int:book_id>', methods=['DELETE'])(delete)
