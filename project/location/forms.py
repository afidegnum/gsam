from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask.ext.wtf import Form
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired
from project.location.models import District, Region, Subdistrict



class DistrictForm(Form):
    district = StringField('District', validators=[DataRequired()])
    region = QuerySelectField(query_factory=lambda: Region.query.filter_by(front=True), allow_blank=True)

class SubdistrictForm(Form):
    subdistrict = StringField('Subdistrict', validators=[DataRequired()])
    district = QuerySelectField(query_factory=lambda: District.query.filter_by(front=True), allow_blank=True)

class VillageForm(Form):
    village = StringField('Village', validators=[DataRequired()])
    lattitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    subdistrict = QuerySelectField(query_factory=lambda: Subdistrict.query.filter_by(front=True), allow_blank=True)