from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('User Name',validators=[DataRequired(message='Please enter your User name')])
    password = PasswordField('Password',validators=[DataRequired(message='Please enter your Password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')