from flask_mail import Message
from re import search
from random import choice
from flask import abort
from itsdangerous import URLSafeTimedSerializer

from server import mail
from server.settings import Settings

def valid_email(email):
  return bool(search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) 

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(Settings.SECRET_KEY)
    return serializer.dumps(email, salt=Settings.SECRET_PASSWORD_SALT)


def confirm_token(token, expiration=60):
    serializer = URLSafeTimedSerializer(Settings.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=Settings.SECRET_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=Settings.MAIL_DEFAULT_SENDER
    )
    mail.send(msg)
