from project import db, bcrypt
from datetime import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from project.deliverables.models import Activity


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    front  = db.Column(db.Boolean, default=True)
    #permissions = db.relationship('Permission', backref='permission')
    users = db.relationship('User', backref='roles')

    def __init__(self, name, front):
        self.name = name
        self.front = front


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True, index=True)
    title = db.Column(db.String(20))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    other_name = db.Column(db.String(40))
    password = db.Column(db.String(255))
    pincode = db.Column(db.String(5))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(70), nullable=False, index=True, unique=True)
    address = db.Column(db.Text)

    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))

    picture = db.Column(db.String(255))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    activation = db.Column(db.String(250))
    active = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, default=datetime.now())
    last_login = db.Column(db.DateTime)
    retries = db.Column(db.Integer)
    remarks = db.relationship('Remark', backref='users', lazy='dynamic')
    projects = db.relationship('Project', backref='users', lazy='dynamic')
    activities_posts = db.relationship('Activity', backref='users', lazy='dynamic')
    # facilitator = db.relationship("Community", back_populates="user")

    def __init__(self,  username, title, password, first_name, last_name, other_name, phone, email, address, region, district, subdistrict, village, picture, role, activation, active, created_date, last_login, retries):
        self.username = username
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.password = bcrypt.generate_password_hash(password, rounds=14)
        self.phone = phone
        self.email = email
        self.address = address
        self.region = region
        self.district = district
        self.subdistrict = subdistrict
        self.village = village
        self.picture = picture
        self.role = role
        self.activation = activation
        self.active = active
        self.created_date = created_date
        self.last_login = last_login
        self.retries = retries

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_annonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)






    def __repr__(self):
        return 'User %r' % self.username



