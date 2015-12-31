from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, RadioField, SelectField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project.models import Role, User



class RoleForm(Form):
    role = StringField('Role Name', validators=[DataRequired(), Length(3, 30)])


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 75), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 50), Regexp('[^A-Za-z][A-Za-z0-9_]$', 0, 'Usernames Must Contains Only Letters, Numbers and Underscore')
                                                   ])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Your Passwords must be same')])
    password2 = PasswordField('Re-Enter Password', validators=[DataRequired()])
    title = SelectField('Title', choices=[('mr', 'Mr'), ('miss', 'MIss'), ('mrs', 'Mrs'), ('dr', 'Dr'), ('prof', 'Prof'), ('el', 'El Hadj'), ('rev', 'Rev'), ('hon', 'Honourable')])
    first_name = StringField('Username', validators=[DataRequired(), Length(1, 50), Regexp('[^A-Za-z]$', 0, 'First Name Must Contains Only Letters')])
    last_name = StringField('Username', validators=[DataRequired(), Length(1, 50), Regexp('[^A-Za-z]$', 0, 'Last Name Must Contains Only Letters')])
    other_names = StringField('Username', validators=[DataRequired(), Length(1, 50), Regexp('[^A-Za-z]$',0, 'Other Names Must Contains Only Letters')])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(1, 75)])
    address = TextAreaField('Your Address', [validators.optional()], validators.length(max=200))
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

