import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


# creating the extension
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'  # similar to url_for() function. Associated with login_required decorator
login_manager.login_message_category = 'info'


mail = Mail()

# from flaskblog import routes

# 🚩have to follow this for running the DB related stuff🚩
# >>> from flaskblog import app, db
# >>> app.app_context().push()
# >>> db.create_all()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handler import errors

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

