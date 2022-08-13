from flask_wtf import Form, FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    TextAreaField,
    validators,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
