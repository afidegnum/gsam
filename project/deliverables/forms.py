from flask.ext.wtf.file import FileRequired, FileAllowed, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from project.location.models import Region, District, Subdistrict, Village
from flask.ext.uploads import UploadSet, IMAGES, DOCUMENTS

__author__ = 'afidegnum'
from flask_wtf import Form
from wtforms.validators import DataRequired, NumberRange
from . models import Sector, Project, Activity
from project import db
from project.crc.models import CrC
from wtforms import StringField, TextAreaField, validators, SubmitField, SelectField, IntegerField, DateTimeField, \
    RadioField, BooleanField, DecimalField, DateField, FileField


class SectorForm(Form):
    name = StringField('Service Sector', validators=[DataRequired()])


def sector_lists():
    return db.session.query(Sector.name)

def region_lists():
    return db.session.query(Region.region)

def district_lists():
    return db.session.query(District.district)

def sub_districts():
    return db.session.query(Subdistrict.subdistrict)

def villages_lists():
    return db.session.query(Village.village)

def project_lists():
    return db.session.query(Project.title)

def activity_lists():
    return db.session.query(Activity.title)

images = UploadSet('images', IMAGES)


class ProjectForm(Form):
    title = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Project Details', validators=[DataRequired()])
    sector = QuerySelectField(get_label='Service Sector', query_factory=sector_lists())
    regions = QuerySelectField(get_label='Regions', query_factory=region_lists())
    district = QuerySelectField(get_label='Regions', query_factory=district_lists())
    subdistrict = QuerySelectField(get_label='Subdistrict', query_factory=sub_districts())
    village = QuerySelectField(get_label='Village', query_factory=villages_lists())
    baseline = TextAreaField('Baseline')
    performance_indicator = TextAreaField('Performance Indicator')
    budget = DecimalField("Planned Budget, places'2'")
    started = DateTimeField('Project Started Date')
    estimated_completion = DateField('Estimated Completion date', format='%Y-%m-%d')
    completed = BooleanField('Completed?', default=False)
    media_gallery = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, "Image Only")
    ])


class BeneficiaryForm(Form):
    name = StringField('Beneficiaries', validators=[DataRequired()])
    descripiton = TextAreaField('Description')
    regions = QuerySelectField(get_label='Regions', query_factory=region_lists())
    district = QuerySelectField(get_label='Regions', query_factory=district_lists())
    subdistrict = QuerySelectField(get_label='Subdistrict', query_factory=sub_districts())
    village = QuerySelectField(get_label='Village', query_factory=villages_lists())

class RemarkForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    Project = QuerySelectField(get_label='Project', query_factory=project_lists())
    activity = QuerySelectField(get_label='Activities', query_factory=activity_lists())
    media_gallery = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, "Image Only")
    ])
    score = SelectField('Rate', validators=[DataRequired()], coerce=int, choices=range(1, 5))




