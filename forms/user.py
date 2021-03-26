from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, NumberRange


class RegisterForm(FlaskForm):
    email = EmailField("Login / email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_again = PasswordField(
        "Repeat password", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[
                       NumberRange(0, 100000000, "Not valid age.")])
    position = StringField("Position", validators=[DataRequired()])
    speciality = StringField("Speciality", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])

    submit = SubmitField("Submit")
