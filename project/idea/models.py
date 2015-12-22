from project import db

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    score = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('category'))
    posted = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.column(db.Integer)
    media = db.Column(db.Integer, db.ForeignKey('media.id'))
    flagged = db.Column(db.Boolean)
    date = db.Column(db.DateTime)
    contest = db.Column(db.Integer, db.ForeignKey('contest.id'))

    def __init__(self, title, description, score, category, posted, author, status, media, flagged):
        self.title = title
        self.description = description
        self.score = score
        self.category = category
        self.posted = posted
        self.author = author
        self.status = status
        self.media = media
        self.flagged = flagged


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    rate = db.column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime)
    idea =  db.Column(db.Integer, db.ForeignKey('idea.id'))

    def __init__(self, title, description, rate, user, date, idea):
        self.title = title
        self.description = description
        self.rate = rate
        self.user = user
        self.date = date
        self.idea = idea


class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text)
    media = db.Column(db.Integer, db.ForeignKey('media.id'))

    def __init__(self, title, start, end, author, description, media):
        self.title = title
        self.start = start
        self.end = end
        self.author = author
        self.description = description
        self.media = media



class Crowdmedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media = db.Column(db.Integer, db.ForeignKey('media.id'))
    contest = db.Column(db.Integer, db.ForeignKey('contest.id'))
    idea = db.Column(db.Integer, db.ForeignKey('idea.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime)

    def __init__(self, media, contest, idea, author, date):
        self.media = media
        self.contest = contest
        self.idea = idea
        self.author = author
        self.date = date
