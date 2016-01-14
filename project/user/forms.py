from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError, SelectField, TextAreaField, validators, \
    BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project import db
from project.models import Role, User
from project.deliverables.forms import region_lists, district_lists, sub_districts, villages_lists


def roles_list():
    r = db.session.query(Role).filter_by(front=True)
    return r


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50, message="You must enter a min and max character")])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Your Passwords must be same')])
    password2 = PasswordField('Re-Enter Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    title = SelectField('Title', choices=[('mr', 'Mr'), ('miss', 'MIss'), ('mrs', 'Mrs'), ('dr', 'Dr'), ('prof', 'Prof'), ('el', 'El Hadj'), ('rev', 'Rev'), ('hon', 'Honourable')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    other_names = StringField('Other Names')
    phone = StringField('Phone Number', validators=[DataRequired()])
    address = TextAreaField('Your Address', [validators.optional()])
    regions = QuerySelectField(get_label='region', query_factory=region_lists)
    district = QuerySelectField(get_label='district', query_factory=district_lists)
    subdistrict = QuerySelectField(get_label='name', query_factory=sub_districts)
    village = QuerySelectField(get_label='village', query_factory=villages_lists)
    roles = QuerySelectField(get_label='name', query_factory=roles_list, allow_blank=True)

    # location = ''
    # picture = ''name for name, in
    # position = ''#Roles
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email address is being used for a similar registration. Is it yours?')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already Registered, is it yours?')



class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me", default=False)
