from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField
from wtforms.fields.simple import BooleanField, EmailField

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='El password es requerido.'),
        validators.length(min=8)
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.DataRequired(message='El email es requerido.'),
        validators.Email(message='Ingrese un email válido.')
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.DataRequired(message='El email es requerido.'),
        validators.Email(message='Ingrese un email válido.')
    ])
    password = PasswordField('Password', [
        validators.DataRequired('El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide.')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])