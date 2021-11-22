from flask import Blueprint
from app.controllers.MainController import index, login, login_post


main_bp = Blueprint('main', __name__)
main_bp.route('/', methods=['GET'])(index)
main_bp.route('/login', methods=['GET'])(login)
main_bp.route('/login-post', methods=['POST'])(login_post)
