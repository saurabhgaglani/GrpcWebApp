from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')