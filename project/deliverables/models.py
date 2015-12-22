from project import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(175), unique=True, nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(20))
    baseline = db.Column(db.Text())
    performance_indicator = db.Column(db.Text)
    budget = db.Column(db.Float())
    remark = db.Column(db.Text())
    remark_author = db.Column(db.Integer, db.ForeignKey('User.id'))
    author = db.Column(db.Integer, db.ForeignKey('User.id')) # backref user
    posted_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    est_completion = db.Column(db.DateTime)
    mark_complete = db.Column(db.Boolean, default=False)
    activities = db.relationship('Activity', backref='projects', cascade='all, delete-orphan', lazy='dynamic')
    remarks = db.relationship('Remark', backref='projects', cascade='all, delete-orphan', lazy='dynamic')
    beneficiary = db.Column(db.Integer, db.ForeignKey('beneficiary.id'))
    #Beneficiary
    #service Sector

    def __init__(self, id, title, description, location, baseline, performance_indicator, budget, remark, remark_author, author, posted_date, start_date, est_completion):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.baseline = baseline
        self.performance_indicator = performance_indicator
        self.budget = budget
        self.remark = remark
        self.remark_author = remark_author
        self.author = author
        self.posted_date = posted_date
        self.start_date = start_date
        self.est_completion = est_completion

class Beneficiary(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(150), nullable=False)
        description = db.Column(db.Text)
        remarks = db.relationship('Project', backref='beneficiary', lazy='dynamic')
        media = ''# db.relationship

        def __init__(self, name, description, remarks, media):
            self.name = name
            self.description = description
            self.remarks = remarks
            self.media = media



class Sector(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(175), unique=True, nullable=False)
        icon = db.Column(db.String(255), nullable=True)

        def __init__(self, name, icon):
            self.name = name
            self.icon = icon


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    allocated_budget= db.Column(db.Float)
    resource = db.Column(db.Text)
    assigned_to = db.Column(db.String(55))
    baseline = db.Column(db.Text)
    remark = db.Column(db.Text)
    remark_author = db.Column(db.Integer, db.ForeignKey('User.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    author = db.Column(db.Integer, db.ForeignKey('User.id'))
    remarks = db.relationship('Remark', backref='activity', cascade='all, delete-orphan', lazy='dynamic')
    est_completion_date = db.Column(db.DateTime)

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


# Location Points from other resources
class LocPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(50), unique=True, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    def __init__(self, id, project_id, activity_id, location_id):
        self.id = id
        self.project_id = project_id
        self.activity_id = activity_id
        self.location_id = location_id

class Remark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, id, name, description, project_id, activity_id, author):
        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.activity_id = activity_id
        self.author = author


