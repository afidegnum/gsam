#from project import db
from flask_sqlalchemy import SQLAlchemy
from project.deliverables.models import Project
db = SQLAlchemy()

class Region(db.Model):
    __tablename__ = 'regions'
    region = db.Column(db.String(30))
    id = db.Column(db.Integer, primary_key=True)
    districts = db.relationship("District", backref='regions')
    # deliverabls
    projects = db.relationship("Project", backref='regions')
    activities = db.relationship("Activity", backref='regions')
    beneficiaries = db.relationship("Beneficiary", backref='regions')
    remarks = db.relationship("Remark", backref='regions')

    def __init__(self, region):
        self.region = region

class District(db.Model):
    __tablename__ = 'districts'
    district = db.Column(db.String(90))
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    subdistricts = db.relationship("Subdistrict", backref='distr')
    # deliverables
    projects = db.relationship("Project", backref='districts')
    activities = db.relationship("Activity", backref='districts')
    beneficiaries = db.relationship("Beneficiary", backref='districts')
    remarks = db.relationship("Remark", backref='districts')


    def __init__(self, id, region_id):
        self.id = id
        self.region_id = region_id

class Subdistrict(db.Model):
    __tablename__ = 'subdistricts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    districts = db.Column(db.Integer, db.ForeignKey('districts.id'))
    villages = db.relationship("Village", backref='subdistricts')
    # deliverables
    projects = db.relationship("Project", backref='subdistricts')
    activities = db.relationship("Activity", backref='subdistricts')
    beneficiaries = db.relationship("Beneficiary", backref='subdistricts')
    remarks = db.relationship("Remark", backref='subdistricts')


    def __init__(self, subdistrict, districts_id):
        self.subdistrict = subdistrict
        self.districts_id = districts_id

class Village(db.Model):
    __tablename__ = 'villages'
    id = db.Column(db.Integer, primary_key=True)
    village = db.Column(db.String(255))
    lattitude = db.Column(db.Float(precision=14))
    longitude = db.Column(db.Float(precision=14))
    subdistrict_id = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    # deliverables
    projects = db.relationship("Project", backref='villages')
    activities = db.relationship("Activity", backref='villages')
    beneficiaries = db.relationship("Beneficiary", backref='villages')
    remarks = db.relationship("Remark", backref='villages')


    def __init__(self, village, lattitude, longitude, subdistrict_id):
        self.village = village
        self.lattitude = lattitude
        self.longitude = longitude
        self.subdistrict_id = subdistrict_id








