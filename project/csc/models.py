from project import db


csmedia = db.Table('cscard_media',
                          db.Column('csc_id', db.Integer, db.ForeignKey('scorecards.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('csc_id', 'media_id'))

class CSC(db.Model):
    __tablename__ = 'scorecards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    sector =  db.Column(db.Integer, db.ForeignKey('sectors.id'))
    age_from = db.Column(db.Integer)
    age_to = db.Column(db.Integer)
    income_from = db.Column(db.Integer)
    income_to = db.Column(db.Integer)
    budget = db.Column(db.Float)
    date = db.Column(db.DateTime)
    media = db.relationship('Media', secondary=csmedia, backref='scorecards')
    agenda = db.relationship('Agenda', backref='scorecards', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, name, description, sector, age_from, age_to, income_from, income_to, budget, date):
        self.name = name
        self.description = description
        self.sector = sector
        self.age_from = age_from
        self.age_to = age_to
        self.income_from = income_from
        self.income_to = income_to
        self.budget = budget
        self.date = date


cscommunity_media = db.Table('cscommunity_media',
                          db.Column('cscommunity_id', db.Integer, db.ForeignKey('cscommunities.id'), nullable=False),
                          db.Column('media_id', db.Integer, db.ForeignKey('media.id'), nullable=False),
                          db.PrimaryKeyConstraint('cscommunity_id', 'media_id'))


class KeyLeader(db.Model):
    __tablename__ = 'keyleaders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.Text)
    community = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    picture = db.Column(db.String(400))

    def __init__(self, name, address, community, picture):
        self.name = name
        self.address = address
        self.community = community
        self.picture = picture


class CSCommunity(db.Model):
    __tablename__ = 'cscommunities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    subgroup = db.Column(db.Text)
    #---------------------------
    region = db.Column(db.Integer, db.ForeignKey('regions.id'))
    district  = db.Column(db.Integer, db.ForeignKey('districts.id'))
    subdistrict  = db.Column(db.Integer, db.ForeignKey('subdistricts.id'))
    village = db.Column(db.Integer, db.ForeignKey('villages.id'))
    agenda = db.relationship('Agenda', backref='community', cascade='all, delete-orphan', lazy='dynamic')
    key_leaders = db.relationship('KeyLeader', backref='cscommunities', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, name, key_leaders, subgroup, region, district, subdistrict, village):
        self.name = name
        self.key_leaders = key_leaders
        self.region = region
        self.district = district
        self.subdistrict = subdistrict
        self.village = village


class Agenda(db.Model):
    __tablename__ = 'communityagenda'
    id = db.Column(db.Integer, primary_key=True)
    scard = db.Column(db.Integer, db.ForeignKey('scorecards.id'))
    crcard = db.Column(db.Integer, db.ForeignKey('crcards.id'))
    cscommunity = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    meeting_date = db.Column(db.DateTime)
    facilitator = db.Column(db.Text)
    notes = db.Column(db.Text)
    submit_date = db.Column(db.DateTime)

    def __init__(self, scard, cscommunity, meeting_date, notes, facilitator, submit_date):
        self.scard = scard
        self.cscommunity = cscommunity
        self.meeting_date = meeting_date
        self.facilitator = facilitator
        self.notes = notes
        self.submit_date = submit_date


class CSinput(db.Model):
    __tablename__ = 'csinput'
    id = db.Column(db.Integer, primary_key=True)
    community = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    cscard = db.Column(db.Integer, db.ForeignKey('scorecards.id'))
    name = db.Column(db.String(100))
    submit_from = db.Column(db.String(25))
    beneficiaries = db.Column(db.String(100))
    indicators = db.Column(db.String(255))
    entitlement = db.Column(db.String(255))
    actuals = db.Column(db.String(255))
    remark = db.Column(db.String(300))
    input_date = db.Column(db.DateTime)

    def __init__(self, community, cscard, name, submit_from, beneficiaries, indicators, entitlements, actuals, remark, input_date):
        self.community = community
        self.cscard = cscard
        self.name = name
        self.submit_from = submit_from
        self.beneficiaries = beneficiaries
        self.indicators = indicators
        self.entitlement = entitlements
        self.actuals = actuals
        self.remark = remark



class CSPerformance(db.Model):
    __tablename__ = 'csperformances'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    community = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    cscard = db.Column(db.Integer, db.ForeignKey('scorecards.id'))
    indicator = db.Column(db.Text)
    score = db.Column(db.String)
    six_month = db.Column(db.Text)
    year = db.Column(db.String(100))
    reasons_for_change = db.Column(db.Text)
    submit_date = db.Column(db.DateTime)

    def __init__(self, name, cscard, indicator, score, six_month, year, reasons_for_change, community, submit_date):
        self.name = name
        self.cscard = cscard
        self.indicator = indicator
        self.score = score
        self.six_month = six_month
        self.year = year
        self.reasons_for_change = reasons_for_change
        self.community=community
        self.submit_date = submit_date

class SelfEvaluation(db.Model):
    __tablename__ = 'csevaluation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    community = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    cscard = db.Column(db.Integer, db.ForeignKey('scorecards.id'))
    performance_criteria = db.Column(db.Text)
    score = db.Column(db.SmallInteger)
    reasons = db.Column(db.Text)
    submit_date = db.Column(db.DateTime)


    def __init__(self, name, community, cscard, performance_criteria, score, reasons, submit_date):
        self.name = name
        self.community - community
        self.performance_criteria = performance_criteria
        self.cscard = cscard
        self.score = score
        self.reasons = reasons
        self.submit_date = submit_date

class ActionPlan(db.Model):
    __tablename__ = 'csactionplan'
    id = db.Column(db.Integer, primary_key=True)
    community = db.Column(db.Integer, db.ForeignKey('cscommunities.id'))
    cscard = db.Column(db.Integer, db.ForeignKey('scorecards.id'))
    improvement = db.Column(db.Text)
    who = db.Column(db.Text)
    when = db.Column(db.String(300))
    proposed_actions = db.Column(db.Text)
    submit_date = db.Column(db.DateTime)

    def __init__(self, cscard, community, improvement, who, when, proposed_actions, submit_date):
        self.cscard = cscard
        self.community = community
        self.improvement = improvement
        self.who = who
        self.when = when
        self.proposed_actions = proposed_actions
        self.submit_date = submit_date
