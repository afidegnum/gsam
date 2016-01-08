from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, NumberRange
from project import db
from project.crc.models import CrC
from project.csc.forms import community_lists
from wtforms import StringField, TextAreaField, validators, SubmitField, SelectField, IntegerField, DateTimeField, \
    RadioField, BooleanField


class CrCForm(Form):
    title = StringField('Title of the CRC project', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    service_target = SelectField('Service Target to study', coerce=int)
    purpose_of_study = TextAreaField('Purpose of Study', validators=[DataRequired()])
    service_scope = TextAreaField('Service Scope', validators=[DataRequired()])
    service_aspect = SelectField('Service Aspect to inspect')

class CommunityForm(Form):
    name = StringField('Name of Community To Visit', validators=[DataRequired()])
    key_leaders = TextAreaField('Influencing leaders of the community')
    facilitators = SelectField('Faciliators of this community', coerce=int)
    subgroup = TextAreaField('SubGroup of interest')
    min_age = IntegerField('Minimum Age of study', [validators.required()])
    max_age = IntegerField('Maximum Age of study', [validators.required()])
    meeting_date = DateTimeField('The Next Meeting date', format='%Y-%m-%d %H:%M')
    region = SelectField('Region', validators=[DataRequired()], coerce=int)
    district = SelectField('District', validators=[DataRequired()], coerce=int)
    subdistrict = SelectField('Subdistrict', validators=[DataRequired()], coerce=int)
    village = SelectField('Village', validators=[DataRequired()], coerce=int)

class BasicQuestionForm(Form):
    name = StringField('Target Name', validators=[DataRequired()])
    gender = RadioField(choices=[('male', 'Male'), ('female', 'Female')])
    community = QuerySelectField(get_label='name', query_factory=community_lists)
    family_type = SelectField('Region', validators=[DataRequired()], coerce=unicode, choices=[('nuclear', 'Nuclear Family'), ('single', 'Single Family'), ('Childless', 'Childless Family'), ('step', 'Step Family'), ('grandparent', 'Grand Parent Family')])
    male_adults = IntegerField('Number of Male adults in the house')
    female_adults = IntegerField('How mane females in the household')
    male_children = IntegerField('Number of male children  in the house')
    female_children = IntegerField('number of Female Children in the house')
    employed = IntegerField('how many of them are employed' )
    traders = IntegerField('How many of them are traders')
    schooling = IntegerField('number of studentse')
    monthly_income = IntegerField('monthly income')

class Aspect(Form):
    StringField('Name of Aspects', validators=[DataRequired()])


class Questions(Form):
    title = StringField('Title of the Question', validators=[DataRequired()])
    type = StringField('Type of Question', description='Select the expected type of answer i.e Yes/No, Numeric etc...', validators=[DataRequired()])

class Answer(Form):
    # start with test question
    numb = IntegerField('Enter your answer')
    strg = StringField('Enter answer')
    yesno = BooleanField('Active')
    rate = IntegerField('Rate', validators=[NumberRange(min=0, max=5)])
