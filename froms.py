from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import  DataRequired

# python class that is representation of Flask-forms
# then we will convert this to html form in blck contnant

class RegistationForm(FlaskForm):
    username = StringField('Username', validators=[])
