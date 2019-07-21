import secrets

class Settings:
    SECRET_KEY = secrets.token_hex(32)
    SECRET_PASSWORD_SALT = secrets.token_hex(4)
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True;
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'bothotelowy@gmail.com'
    MAIL_PASSWORD = 'A123321A'
    MAIL_DEFAULT_SENDER = 'LSD'
    
    REGISTRATION_ENAGLED = True

class Discord:
    url = 'https://discord.gg/djWqZGu'
    s_id = '223072196887707648'
    ch_id = '592333511449378826'
