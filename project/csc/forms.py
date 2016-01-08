from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators, FloatField, DateTimeField
from wtforms.validators import DataRequired
from project import db
from project.csc.models import CSCommunity, CSC
from flask_wtf.file import FileField, FileRequired
from project.deliverables.forms import sector_lists, region_lists, district_lists, sub_districts, villages_lists

def community_lists():
    return db.session.query(CSCommunity)

def score_cards():
    return db.session.query(CSC)


class CSForm(Form):
    name = StringField('Title of the CSC Card', validators=[DataRequired()])
    description = TextAreaField('description')
    sector = QuerySelectField(get_label='name', query_factory=sector_lists)
    age_from = IntegerField('minimum age', [validators.required()])
    age_to = IntegerField('maximum age', [validators.required()])
    income_from = IntegerField('minimum ingome', [validators.required()])
    income_to = IntegerField('maximum income', [validators.required()])
    budget = FloatField('Budget for this project')
    media = FileField('Upload Media', validators=[FileRequired()])


class CsCommunityform(Form):
    name = StringField('Community to visitt', validators=[DataRequired()])
    regions = QuerySelectField(get_label='region', query_factory=region_lists)
    district = QuerySelectField(get_label='district', query_factory=district_lists)
    subdistrict = QuerySelectField(get_label='subdistrict', query_factory=sub_districts)
    village = QuerySelectField(get_label='village', query_factory=villages_lists)
    subgroup = TextAreaField('The SUbgroup of interest')
    media = FileField('Upload Media', validators=[FileRequired()])

class AgendaForm(Form):
    score_card = QuerySelectField(get_label='name', query_factory=score_cards)
    community = QuerySelectField(get_label='name', query_factory=community_lists)
    meeting_date = DateTimeField('The Next Meeting date', format='%Y-%m-%d %H:%M')
    facilitators = TextAreaField('Facilitators')
    notes = TextAreaField('Notes')



class KeyLeadersForm(Form):
    name = StringField('Name of Facilitator')
    address = TextAreaField('Address')
    picture = FileField('Upload Picture', validators=[FileRequired()])
    community = QuerySelectField(get_label='name', query_factory=community_lists)


class CSInputform(Form):
    name = StringField('Input Name', validators=[DataRequired()])
    beneficiaries = StringField('Beneficiaries', validators=[DataRequired()])
    indicators = TextAreaField('Indicators')
    entitlements = TextAreaField('Indicators')
    actuals = TextAreaField('Actual situation')
    remark = TextAreaField('Remark')

class CSPerformanceForm(Form):
    name = StringField('name', validators=[DataRequired()])
    indicator = TextAreaField('Indicators')
    score = IntegerField('Score', [validators.required()])
    six_month = TextAreaField('After Six Months')
    year_later = TextAreaField('after a year, ')
    reasons_for_change = TextAreaField('Reasons for change')

class SelfEvaluationForm(Form):
    name = StringField('Title of the evaluation', validators=[DataRequired()])
    performance_criteria = TextAreaField('Performance Criteria', validators=[DataRequired()])
    score = IntegerField('Score', [validators.required()])
    reasons = TextAreaField('Reasons for change', validators=[DataRequired()])

class ActionPlanForm(Form):
    improvement = TextAreaField('Improvement', validators=[DataRequired()])
    who = TextAreaField('Who will take action', validators=[DataRequired()])
    when = TextAreaField('When will that action taken', validators=[DataRequired()])
    proposed_actions = TextAreaField('Proposed Actions', validators=[DataRequired()])