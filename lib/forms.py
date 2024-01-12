from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, EmailField, IntegerField, DateField
from wtforms.validators import InputRequired, Length, Regexp, Email, DataRequired
from wtforms.widgets import NumberInput, Input, DateInput
from flask_wtf.file import FileField, FileAllowed, FileRequired

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
        InputRequired(),
        Regexp(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).*$',
               message="Password must contain at least 1 UpperCase, 1 Number, and 1 special character"),
        Length(min=8)
    ], render_kw={"placeholder": "Password"})
    email = EmailField(validators=[InputRequired(), Length(min=8, max=100)], render_kw={"placeholder": "Email"})
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

class NewListingForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Name"})
    address = StringField(validators=[InputRequired()], render_kw={"placeholder": "Address"})
    price = IntegerField('Price', validators=[validators.NumberRange(min=0, max=10000)], widget=NumberInput())
    image_path = FileField('Image', validators=[
        FileRequired(),  
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!') 
    ])
    description = StringField(validators=[InputRequired()], render_kw={"placeholder": "Description"})
    date_added = DateField('Date Added', format='%Y-%m-%d', validators=[DataRequired()], widget=DateInput())
    submit = SubmitField('Submit')


class BookingForm(FlaskForm):
    booking_date = DateField('Date Added', format='%Y-%m-%d', validators=[DataRequired()], widget=DateInput())
    submit = SubmitField('Submit')
