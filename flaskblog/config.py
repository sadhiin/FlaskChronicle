class Config:
    # Best practices: https://youtu.be/Wfx4YBzg16s?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
    SECRET_KEY = '8be8ee977461bc714355f66f4be67f81'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    MAIL_USERNAME = "devdummay150@gmail.com"
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    MAIL_PASSWORD = "1qaz1qaz!Q"
