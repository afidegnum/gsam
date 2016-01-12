from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError, SelectField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project.models import Role, User
from project.deliverables.forms import region_lists, district_lists, sub_districts, villages_lists



class RoleForm(Form):
    role = StringField('Role Name', validators=[DataRequired(), Length(3, 30)])


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50, message="You must enter a min and max character"), Regexp('[^A-Za-z][A-Za-z0-9_]$', 0, 'Usernames Must Contains Only Letters, Numbers and Underscore')
                                                   ])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Your Passwords must be same')])
    password2 = PasswordField('Re-Enter Password', validators=[DataRequired()])
    title = SelectField('Title', choices=[('mr', 'Mr'), ('miss', 'MIss'), ('mrs', 'Mrs'), ('dr', 'Dr'), ('prof', 'Prof'), ('el', 'El Hadj'), ('rev', 'Rev'), ('hon', 'Honourable')])
    first_name = StringField('Username', validators=[DataRequired(), Regexp('[^A-Za-z]$', 0, 'First Name Must Contains Only Letters')])
    last_name = StringField('Username', validators=[DataRequired(), Regexp('[^A-Za-z]$', 0, 'Last Name Must Contains Only Letters')])
    other_names = StringField('Username', validators=[DataRequired(), Regexp('[^A-Za-z]$',0, 'Other Names Must Contains Only Letters')])
    phone = StringField('Phone Number', validators=[DataRequired()])
    address = TextAreaField('Your Address', [validators.optional()])
    regions = QuerySelectField(get_label='region', query_factory=region_lists)
    district = QuerySelectField(get_label='district', query_factory=district_lists)
    subdistrict = QuerySelectField(get_label='subdistrict', query_factory=sub_districts)
    village = QuerySelectField(get_label='village', query_factory=villages_lists)
    roles = QuerySelectField(query_factory=lambda: Role.query.filter_by(front=True), allow_blank=True)

    # location = ''
    # picture = ''
    # position = ''#Roles
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email address is being used for a similar registration. Is it yours?')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already Registered, is it yours?')

