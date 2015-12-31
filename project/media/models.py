from project import db
from datetime import datetime


class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    location = db.Column(db.String(150))
    author = db.Column(db.ForeignKey('users.id'))
    posted_date = db.Column(db.DateTime(), default=datetime.utcnow)







