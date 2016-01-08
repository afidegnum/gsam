from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project.location.models import Region, District, Subdistrict, Village
#from flask.ext.uploads import UploadSet, IMAGES, DOCUMENTS
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, NumberRange
from . models import Sector, Project, Activity
from project import db
from project.crc.models import CrC
from wtforms import StringField, TextAreaField, validators, SubmitField, SelectField, IntegerField, DateTimeField, \
    RadioField, BooleanField, DecimalField, DateField




def sector_lists():
    return db.session.query(Sector)

def region_lists():
    return db.session.query(Region)

def district_lists():
    return db.session.query(District)

def sub_districts():
    return db.session.query(Subdistrict)

def villages_lists():
    return db.session.query(Village)

def project_lists():
    return db.session.query(Project)

def activity_lists():
    return db.session.query(Activity)

class SectorForm(Form):
    name = StringField('Service Sector', validators=[DataRequired()])

#images = UploadSet('images', IMAGES)


class ProjectForm(Form):
    title = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Project Details', validators=[DataRequired()])
    sector = QuerySelectField(get_label='name', query_factory=sector_lists)
    regions = QuerySelectField(get_label='region', query_factory=region_lists)
    district = QuerySelectField(get_label='district', query_factory=district_lists)
    subdistrict = QuerySelectField(get_label='subdistrict', query_factory=sub_districts)
    village = QuerySelectField(get_label='village', query_factory=villages_lists)
    baseline = TextAreaField('Baseline')
    performance_indicator = TextAreaField('Performance Indicator')
    budget = DecimalField("Planned Budget", places=2)
    started = DateTimeField('Project Started Date')
    estimated_completion = DateField('Estimated Completion date', format='%Y-%m-%d')
    #completed = BooleanField('Completed?', default=False)
    media_gallery = FileField('image', validators=[FileRequired()])


class BeneficiaryForm(Form):
    name = StringField('Beneficiaries', validators=[DataRequired()])
    descripiton = TextAreaField('Description')
    regions = QuerySelectField(get_label='region', query_factory=region_lists)
    district = QuerySelectField(get_label='district', query_factory=district_lists)
    subdistrict = QuerySelectField(get_label='subdistrict', query_factory=sub_districts)
    village = QuerySelectField(get_label='village', query_factory=villages_lists)
    media_gallery = FileField('image', validators=[FileRequired()])

class RemarkForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    Project = QuerySelectField(get_label='Project', query_factory=project_lists)
    activity = QuerySelectField(get_label='Activities', query_factory=activity_lists)
    media_gallery = FileField('image', validators=[
        FileRequired()
    ])
    score = SelectField('Rate', validators=[DataRequired()], coerce=int, choices=range(1, 5))




