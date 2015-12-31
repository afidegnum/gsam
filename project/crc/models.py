from project import db

class CrC(db.Model):
    __tablename__ = 'crcards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    service_target = db.Column(db.Integer, db.ForeignKey('sectors.id'))
    service_scope = db.Column(db.Text)
    purpose_of_study = db.Column(db.Text)
    service_aspect = db.Column(db.Integer, db.ForeignKey('aspects.id'))
    date = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __init__(self, title, description, service_target, purpose_of_study, service_aspect):
        self.title = title
        self.description = description
        self.service_target = service_target
        self.purpose_of_study = purpose_of_study
        self.service_aspect = service_aspect

class Community(db.Model):
    __tablename__ = 'communities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    key_leaders = db.Column(db.Text)
    facilitators_id = db.Column(db.Integer, db.ForeignKey('users.id')) # or add plain
    facilitators = db.relationship("User")
    subgroup = db.Column(db.Text)
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    meeting_date = db.Column(db.DateTime)
    #---------------------------
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))
    #------------------------------------

    def __init__(self, name, district, key_leaders, facilitators, subgroup, min_age, max_age, meeting_date):
        self.name = name
        self.district = district
        self.key_leaders = key_leaders
        self.facilitators = facilitators
        self.subgroup = subgroup
        self.min_age = min_age
        self.max_age = max_age
        self.meeting_date = meeting_date


class BasicQuestion(db.Model):
    __tablename__ = 'basic_questions'
    id = db.Column(db.Integer, primary_key=True)
    investigator = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(150))
    gender = db.Column(db.String(7))
    location = db.Column(db.Integer, primary_key=True)
    family_type = db.Column(db.String(20))
    male_adults = db.Column(db.Integer)
    female_adults = db.Column(db.Integer)
    male_children = db.Column(db.Integer)
    female_children = db.Column(db.Integer)
    employed = db.Column(db.Integer)
    students = db.Column(db.Integer)
    traders = db.Column(db.Integer)
    monthly_income = db.Column(db.Float)
    date = db.Column(db.DateTime)
    #---------------------------
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))
    #------------------------------------

    def __init__(self, investigator, name, gender, location, family_type, male_adults, female_adults, male_children, female_children, employed, students, traders, monthly_income, date):
        self.investigator = investigator
        self.gender = gender
        self.location = location
        self.family_type = family_type
        self.male_adults = male_adults
        self.female_adults = female_adults
        self.male_children = male_children
        self.female_children = female_children
        self.employed = employed
        self.students = students
        self.traders = traders
        self.monthly_income = monthly_income
        self.date = date

class Aspect(db.Model):
    __tablename__ = 'aspects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    type = db.Column(db.Integer)
    answers = db.relationship('Answer', backref='questions')

    def __init__(self, title, type):
        self.title = title
        self.type = type


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Integer, db.ForeignKey('questions.id'))
    plain = db.Column(db.String(255), nullable=True)
    numeric = db.Column(db.Integer, nullable=True)
    yesno = db.Column(db.Boolean, nullable=True)
    rate = db.Column(db.Integer)
    #---------------------------
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))
    #------------------------------------

    def __init__(self, question, plain, numeric, yesno, rate):
        self.question = question
        self.plain = plain
        self.numeric = numeric
        self.yesno = yesno
        self.rate = rate


