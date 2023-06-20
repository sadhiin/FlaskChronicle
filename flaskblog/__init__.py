from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8be8ee977461bc714355f66f4be67f81'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# creating the extension
db = SQLAlchemy(app)

from flaskblog import routes

# >>> from flaskblog import app, db
# >>> app.app_context().push()
# >>> db.create_all()
