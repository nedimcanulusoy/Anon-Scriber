from anon_scriber import app
from anon_scriber.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, DataRequired, EqualTo, Email
from anon_scriber import datetime

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError("This username is already taken! Please try a different username.")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()

        if email_address:
            raise ValidationError("This email address is already in use! Please try a different email address.")


    username = StringField(label='Username', validators=[Length(min=2, max=50), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    re_password = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    email_address = StringField(label='Email Address')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')

class PostForm(FlaskForm):
    title = StringField(label='Title: ', validators=[Length(min=1, max=60), DataRequired()])
    post_text = TextAreaField(label='Your Post: ', validators=[Length(min=1, max=1024), DataRequired()])
    time_stamp_of_post = StringField(label="Posted on: ", default=datetime.utcnow)
    submit = SubmitField(label='Share')


