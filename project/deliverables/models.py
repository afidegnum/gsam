from project import db
from flask.ext.sqlalchemy import SQLAlchemy
from project.media.models import Media


projects_media = db.Table('project_media',
                          db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('project_id', 'media_id'))
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(175), unique=True, nullable=False)
    description = db.Column(db.Text)
    #---------------------------
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))
    #------------------------------------
    baseline = db.Column(db.Text())
    performance_indicator = db.Column(db.Text)
    budget = db.Column(db.Float())
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    est_completion = db.Column(db.DateTime)
    mark_complete = db.Column(db.Boolean, default=False)
    activities = db.relationship('Activity', backref='projects', cascade='all, delete-orphan', lazy='dynamic')
    remarks = db.relationship('Remark', backref='projects', cascade='all, delete-orphan', lazy='dynamic')
    beneficiary = db.Column(db.Integer, db.ForeignKey('beneficiaries.id'))
    sector =  db.Column(db.Integer, db.ForeignKey('sectors.id'))
    media = db.relationship('Media', secondary=projects_media, backref='projects')

    def __init__(self, id, title, description, baseline, performance_indicator, budget, remark, remark_author, author, posted_date, start_date, est_completion, mark_complete):
        self.id = id
        self.title = title
        self.description = description
        self.baseline = baseline
        self.performance_indicator = performance_indicator
        self.budget = budget
        self.author = author
        self.posted_date = posted_date
        self.start_date = start_date
        self.est_completion = est_completion
        self.mark_complete = mark_complete


beneficiaries_media = db.Table('beneficiaries_media',
                          db.Column('beneficiary_id', db.Integer, db.ForeignKey('beneficiaries.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('beneficiary_id', 'media_id'))

class Beneficiary(db.Model):
    __tablename__ = 'beneficiaries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text)
    projects = db.relationship('Project', backref='beneficiaries', lazy='dynamic')
    media = db.relationship('Media', secondary=beneficiaries_media, backref='beneficiaries')
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))

    def __init__(self, name, description, remarks, media):
        self.name = name
        self.description = description
        self.remarks = remarks
        self.media = media


class Sector(db.Model):
    __tablename__ = 'sectors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    projects = db.relationship('Project', backref='secto', lazy='dynamic')

    def __init__(self, name):
        self.name = name


activities_media = db.Table('activities_media',
                          db.Column('activity_id', db.Integer, db.ForeignKey('activities.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('activity_id', 'media_id'))



class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    allocated_budget= db.Column(db.Float)
    resource = db.Column(db.Text)
    assigned_to = db.Column(db.String(55))
    baseline = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    remarks = db.relationship('Remark', backref='activities', cascade='all, delete-orphan', lazy='dynamic')
    est_completion_date = db.Column(db.DateTime)
    media = db.relationship('Media', secondary=activities_media, backref='activities')
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))

    def __init__(self, id, title, description, allocated_budget, resource, assigned_to, baseline, remark, remark_author, project_id, author, est_completion_date):
        self.id = id
        self.title = title
        self.description = description
        self.allocated_budget = allocated_budget
        self.resource = resource
        self.assigned_to = assigned_to
        self.baseline = baseline
        self.project_id = project_id
        self.author = author
        self.est_completion_date = est_completion_date


remarks_media = db.Table('remarks_media',
                          db.Column('remark_id', db.Integer, db.ForeignKey('remarks.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('remark_id', 'media_id'))

class Remark(db.Model):
    __tablename__ = 'remarks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    media = db.relationship('Media', secondary=remarks_media, backref='remarks')
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))

    def __init__(self, id, name, description, project_id, activity_id, author):
        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.activity_id = activity_id
        self.author = author


