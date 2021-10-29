from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
#from _typeshed import OpenBinaryMode, OpenBinaryModeReading
from flask import render_template #método para renderizar templates HTML
from flask import request
from app import app, db
from app.models.tables import Pessoa, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from re import *

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = Usuario.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logado!", category='success')
                #login_user(user, remember=True)
                return True
            else:
                flash('Senha incorreta.', category='error')
        else:
            flash('O email informado não existe', category='error')

    return flash('Método de solicitação incompatível', category='error')


"""
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = Usuario.query.filter_by(email=email).first()

        if email_exists:
            flash('O email informado já está sendo utilizado.', category='error')
        elif password1 != password2:
            flash('As senhas não coincidem', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = Usuario(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))"""