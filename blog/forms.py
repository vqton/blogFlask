from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class LoginForm(Form):
    username = StringField(
        "Username",
    )
    password = PasswordField(
        "Password",
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
