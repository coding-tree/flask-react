from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from server import db, login_manager
from flask_login import UserMixin
 
from datetime import datetime

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

user_tickets = db.Table('user_tickets',
    db.Column('ticket_id', db.Integer, db.ForeignKey('ticket.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, nullable=False, default=6)
    tickets = db.relationship('Ticket', secondary=user_tickets, lazy='subquery',
        backref=db.backref('tickets', lazy=True))
    title = db.Column(db.String(30), nullable=True, default='Użytkownik')
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(25), unique=False, nullable=False,
                             default='../static/default.png')
    registered_on = db.Column(db.Date)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "User:" + self.username

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    desc = db.Column(db.String(260), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return "Product:" + self.name

ticket_replies = db.Table('ticket_replies',
    db.Column('ticket_id', db.Integer, db.ForeignKey('ticket.id')),
    db.Column('reply_id', db.Integer, db.ForeignKey('replies.id'))
)

class Replies(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.String(1500))
    reply_user = db.Column(db.String(20))
    reply_on = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return "Reply:" + self.reply_user

class Ticket(db.Model):
    __tablename__= 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default='OPEN')
    user = db.relationship('User', secondary=user_tickets, lazy='subquery',
        backref=db.backref('user', lazy=True, uselist=False))
    subject = db.Column(db.String(120), unique=False, nullable=False)
    message = db.Column(db.String(1500))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
    replies = db.relationship('Replies', secondary=ticket_replies, lazy='subquery',
        backref=db.backref('replies', lazy=True))

    def __repr__(self):
        return "Ticket:" + self.subject


