from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators, FloatField, DateTimeField
from wtforms.validators import DataRequired


class CSForm(Form):
    name = StringField('Title of the CSC Card', validators=[DataRequired()])
    description = TextAreaField('description')
    sector = SelectField('Sector')
    age_from = IntegerField('minimum age', [validators.required()])
    age_to = IntegerField('maximum age', [validators.required()])
    income_from = IntegerField('minimum ingome', [validators.required()])
    income_to = IntegerField('maximum income', [validators.required()])
    budget = FloatField('Budget for this project')


class CsCOmmunityform(Form):
    name = StringField('Community to visitt', validators=[DataRequired()])
    region = SelectField('Region', validators=[DataRequired()], coerce=int)
    district = SelectField('District', validators=[DataRequired()], coerce=int)
    subdistrict = SelectField('Subdistrict', validators=[DataRequired()], coerce=int)
    village = SelectField('Village', validators=[DataRequired()], coerce=int)
    key_leaders = TextAreaField('Key Leaders')
    facilitators = SelectField('Key Leaders')
    subgroup = TextAreaField('The SUbgroup of interest')
    meeting_date = DateTimeField('The Next Meeting date', format='%Y-%m-%d %H:%M')


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
