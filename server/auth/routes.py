from flask import url_for, redirect, request, Blueprint, abort, jsonify
from flask_login import login_user, current_user, logout_user, login_required, AnonymousUserMixin

from itsdangerous import SignatureExpired, BadSignature

from server.settings import Settings, Discord
from server.auth.utils import (valid_email, send_email,
                         generate_confirmation_token, confirm_token)
from server.models import User
from server import db, bcrypt, s

from datetime import datetime

auth = Blueprint('auth', __name__)

class BadToken(Exception):
    pass

@auth.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    print(username, password)
    if username is None or password is None:
        return jsonify(result={
            'message':'Pola nie mogą być puste.',
            'category':'warning'
        }), 422
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
    else: 
        return jsonify(result={
            'message':'Błędny login lub hasło.',
            'category':'warning'
        }), 422
    return jsonify(result={
        'message':'Zostałeś pomyślnie zalogowany.',
        'category':'success',
    })

@auth.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    mail = request.json.get('email')
    user = User.query.filter_by(username=username).first()
    email = User.query.filter_by(email=mail).first()
    if user:
        return jsonify(result={
            'message':'Konto o podanej nazwie użytkownika już istnieje.',
            'category':'danger'
        })
    if email:
        return jsonify(result={
            'message':'Konto o podanym adresie email już istnieje!',
            'category':'danger'
        })
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    newUser = User(username=username, password=hashed_password, 
                    email=mail, registered_on=datetime.now())
    token = generate_confirmation_token(newUser.email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    subject = "Potwierdź swoje konto"
    send_email(newUser.email, subject, confirm_url)
    db.session.add(newUser)
    db.session.commit()
    return jsonify(result={
        'message':'Rejestracja przebiegła pomyślnie, na podany adres email została wysłana wiadomość z linkiem wymaganym do dokończenia rejestracji.',
        'category':'succes'
    })

@auth.route('/api/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try: 
        email = confirm_token(token)
        if not confirm_token(token):
            raise BadToken()
        user = User.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return jsonify(result={
                'message':'To konto zostało już aktywowane.',
                'category':'info'
            })
        else: 
            user.confirmed = True
            db.session.add(user)
            db.session.commit()
    except BadToken:
        return jsonify(result={
            'message':'Link aktywacyjny wygasł, lub jest nieprawidłowy! skontaktuj się z administratorem serwisu.',
            'category':'warning'
        })
    return jsonify({'message': 'Twoje konto zostało pomyślnie aktywowane!'})

@auth.route('/api/resetpassword', methods=['POST'])
def reset_password_request():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('auth.reset_password', token=token, _external=True)
        subject = "Zresetuj hasło"
        send_email(user.email, subject, confirm_url)
    else: 
        return jsonify(result={
            'message':'Użytkownik o podanym emailu nie istnieje!',
            'category':'warning'
        })
    return jsonify(result={
        'message':'Na podany adres email wysłaliśmy wiadomość z instrukcja zresetowania hasła',
        'category':'info'
    })

tokens = []
@auth.route('/api/reset/<token>', methods=['POST'])
def reset_password(token):
    global tokens
    try:
        if not confirm_token(token):
            raise BadToken()
        if [token for t in tokens]:
            raise BadToken()
        email = confirm_token(token)
        user = User.query.filter_by(email=email).first_or_404()
        password = request.json.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user.password = hashed_password
        tokens.append(token)
        db.session.commit()
    except BadToken:
        return jsonify(result={
                'message': 'Link resetowania hasła wygasł lub jest nieprawidłowy, skontaktuj się z administratorem serwisu',
                'category': 'warning'
        })
    return jsonify(result={
        'message':'Hasło do konta zostało pomyślnie zresetowane.',
        'category':'success'
    })

@auth.route('/api/resendconfirm', methods=['GET'])
def resend_confirm_token():
    user = User.query.filter_by(username="LSD124").first()
    login_user(user)
    email = current_user.email
    token = generate_confirmation_token(email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    send_email(email, "Potwierdź swoje konto", confirm_url)
    return jsonify({
        'msg':'Na podany adres został wysłany link potwierdający',
        'category':'info'
    })