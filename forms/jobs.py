from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, DateTimeField, IntegerField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime


class JobsForm(FlaskForm):
    job = StringField("Job", validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[
                             NumberRange(0, 100000000, "Not valid age.")])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    start_date = DateTimeField("Start date", default=datetime.now())
    end_date = DateTimeField("End date", default=datetime.now())
    is_finished = BooleanField("Is finished")
    submit = SubmitField('Confirm')
