from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
=======
from wtforms import StringField, PasswordField, SubmitField, BooleanField
>>>>>>> 8361315c0d6896a768f4155f66e03368e71a5a2c
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from flask_login import current_user
from application.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20),
                                       Regexp('^\w+$',
                                              message='Username can contain only letters, numbers or underscore.')])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(max=120),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(max=100),
                                         Regexp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',
                                                message=('Password must contain at least eight characters, at least one number, lowercase letter, uppercase letter, and special character (e.g. #?!@$%^&*-).'))])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 Length(max=100),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(max=120),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(max=100)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20),
                                       Regexp('^\w+$',
                                              message='Username can contain only letters, numbers or underscore.')])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(max=120),
                                    Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class ResetRequestForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(max=120),
                                    Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. Please register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(max=100),
                                         Regexp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$',
                                                message=('Password must contain at least eight characters, at least one number, lowercase letter, uppercase letter, and special character (e.g. #?!@$%^&*-).'))])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 Length(max=100),
                                                 EqualTo('password')])
    submit = SubmitField('Reset Password')
