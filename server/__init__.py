from flask_bcrypt import Bcrypt
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer

from server.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Anonymous'
    self.title = ''
    self.email = ''
    self.image_file = ''
    self.registered_on = ''


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(Settings.SECRET_KEY)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.anonymous_user = Anonymous



from server.auth.routes import auth
from server.home.routes import home_bp
from server.profile.routes import profile
from server.market.routes import market
app.register_blueprint(auth)
app.register_blueprint(home_bp)
app.register_blueprint(profile)
app.register_blueprint(market)

