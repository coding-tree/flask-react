from datetime import datetime
from server import db, login_manager
from flask_login import UserMixin
 
from datetime import datetime

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, nullable=False, default=6)
    title = db.Column(db.String(30), nullable=True, default='Użytkownik')
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(25), unique=False, nullable=False,
                             default='../static/default.png')
    registered_on = db.Column(db.Date)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"{self.username}, {self.email}, {self.title}, {self.registered_on}, {self.image_file}"

class Market(db.Model):
    __tablename__ = 'market'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    desc = db.Column(db.String(260), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    add_date = db.Column(db.DateTime, nullable=False , default=datetime.now())

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}"

