import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '8be8ee977461bc714355f66f4be67f81'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# creating the extension
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # similar to url_for() function. Associated with login_required decorator
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_USERNAME'] = "devdummay150@gmail.com"
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_PASSWORD'] = "1qaz1qaz!Q"
mail = Mail(app)



from flaskblog import routes

# 🚩have to follow this for running the DB related stuff🚩
# >>> from flaskblog import app, db
# >>> app.app_context().push()
# >>> db.create_all()
