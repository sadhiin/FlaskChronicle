from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '8be8ee977461bc714355f66f4be67f81'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# creating the extension
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # similar to url_for() function. Associated with login_required decorator
login_manager.login_message_category = 'info'

from flaskblog import routes

# 🚩have to follow this for running the DB related stuff🚩
# >>> from flaskblog import app, db
# >>> app.app_context().push()
# >>> db.create_all()
