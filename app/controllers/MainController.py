from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User, Client, Employee
from werkzeug.security import check_password_hash

def index():
    if current_user.is_authenticated:
        if isinstance(current_user, Client):
            # return "Client view."
            return render_template('base.html',name=current_user.name)
            # return redirect(url_for(''))
        elif isinstance(current_user, Employee):
            return "Employee view."
        else:
            return "Logout."
    else:
        return redirect(url_for('main.login'))


def login():
    return render_template('login.html')

# @auth.route('/login-post', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        flash('Brak użytkownika o loginie %s' % email)
        return redirect(url_for('main.index'))

    if not check_password_hash(user.password, password):
        flash('Błędne hasło')
        return redirect(url_for('main.index'))

    login_user(user)
    return redirect(url_for('main.index'))

@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
