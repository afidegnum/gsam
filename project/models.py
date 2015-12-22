from project import db
from datetime import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from project.location.models import Village

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    front  = db.Column(db.Boolean, default=True)
    #permissions = db.relationship('Permission', backref='permission')
    users = db.relationship('Users', backref='roles')

    def __init__(self, name, front):
        self.name = name
        self.front = front


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, index=True)
    title = db.Column(db.String(20))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    other_name = db.Column(db.String(40))
    password = db.Column(db.String(255))
    pincode = db.Column(db.String(5))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(70), nullable=False, index=True, unique=True)
    address = db.Column(db.Text)
    location = db.Column(db.Integer, db.ForeignKey('villages.id'))
    picture = db.Column(db.String(255))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    activation = db.Column(db.String(250))
    active = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, default=datetime.now())
    last_login = db.Column(db.DateTime)
    retries = db.Column(db.Integer)

    def __init__(self,  username, title, first_name, last_name, other_name, password, phone, email, address, location, picture, role, activation, active, created_date, last_login, retries):
        self.username = username
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.password = password
        self.phone = phone
        self.email = email
        self.address = address
        self.location = location
        self.picture = picture
        self.role = role
        self.activation = activation
        self.active = active
        self.created_date = created_date
        self.last_login = last_login
        self.retries = retries

    def __repr__(self):
        return 'User %r' % self.name

    @property
    def password(self):
        raise AttributeError('Thief! Hacker! Do you think you can go away with this? Your days are Numbered! Start Running')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


