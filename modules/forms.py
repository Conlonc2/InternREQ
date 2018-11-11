from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Login(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[
                             DataRequired(), Length(min=6, max=255)])
    submit = SubmitField('Login')


class Registration(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    user_type = SelectField('Account Type: ', validators=[DataRequired()], choices=[
        ('student', 'Student'), ('faculty', 'Faculty'), ('sponsor', 'Sponsor')])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[
        DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password:  ', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Register ', validators=[DataRequired()])


class Posting(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    overview = TextAreaField('Overview', validators=[])
    responsibilities = TextAreaField('Responsibilities', validators=[])
    reqs = TextAreaField('Applicant Requirments', validators=[])
    comp = SelectField('Compensation', validators=[DataRequired()], choices=[
                       ('1', 'Yes'), ('0', "No")])
    fullPart = SelectField('Internship/Part/Full time',
                           validators=[DataRequired()],
                           choices=[('Internship', 'Internship'), ('Part-Time', 'Part-Time'), ('Full-Time', 'Full Time')])
    hours = TextAreaField('Hours (Day: required hours)',
                          validators=[DataRequired()])

    '''
    Put more fields here
    '''

    submit = SubmitField('Create Posting ', validators=[DataRequired()])
