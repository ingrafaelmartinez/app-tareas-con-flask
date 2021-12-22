from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=8)
    ])