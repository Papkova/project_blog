from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    confirm = PasswordField("Confirm Password: ", validators=[DataRequired(), EqualTo(
        "password",
        message="Password must match"
    )])
    submit = SubmitField("Register")

    # def validate_username(self, username):
    #     sing = Sing.query.filter_by(username=username.data)
