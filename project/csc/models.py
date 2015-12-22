from project import db


class CSC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    sector = db.Column(db.Integer, db.ForeignKey('sector.id'))
    age_from = db.Column(db.Integer)
    age_to = db.Column(db.Integer)
    income_from = db.Column(db.Integer)
    income_to = db.Column(db.Integer)
    budget = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __init__(self, name, description, sector, age_from, age_to, income_from, income_to, budget, date):
        self.name = name
        self.description = description
        self.sector = sector
        self.age_from = age_from
        self.age_to = age_to
        self.income_from = income_from
        self. income_to = income_to
        self.budget = budget
        self.date = date

class CSCommunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    district = db.Column(db.Integer, db.ForeignKey('location.id'))
    key_leaders = db.Column(db.Text)
    facilitators = db.Column(db.Integer, db.ForeignKey('user.id')) # or add plain
    subgroup = db.Column(db.Text)
    meeting_date = db.Column(db.DateTime)

    def __init__(self, name, district, key_leaders, facilitators, subgroup, meeting_date):
        self.name = name
        self.district = district
        self.key_leaders = key_leaders
        self.facilitators = facilitators
        self.meeting_date = meeting_date


class CSinput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    submit_from = db.Column(db.String(25))
    beneficiaries = db.Column(db.String(100))
    indicators = db.Column(db.String(255))
    entitlement = db.Column(db.String(255))
    actuals = db.Column(db.String(255))
    remark = db.Column(db.String(300))

    def __init__(self, name, location, submit_from, beneficiaries, indicators, entitlement, actuals, remark):
        self.name = name
        self.location = location
        self.submit_from = submit_from
        self.beneficiaries = beneficiaries
        self.indicators = indicators
        self.entitlement = entitlement
        self.actuals = actuals
        self.remark = remark



class CSPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    indicator = db.Column(db.Text)
    score = db.Column(db.String)
    six_month = db.Column(db.String(100))
    year = db.Column(db.String(100))
    reasons_for_change = db.Column(db.Text)

    def __init__(self, name, location, indicator, score, six_month, year, reasons_for_change):
        self.name = name
        self.location = location
        self.indicator = indicator
        self.score = score
        self.six_month = six_month
        self.year = year
        self.reasons_for_change = reasons_for_change

class SelfEvaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    performance_criteria = db.Column(db.Text)
    score = db.Column(db.SmallInteger)
    reasons = db.Column(db.Text)

    def __init__(self, name, performance_criteria, score, reasons):
        self.name = name
        self.performance_criteria = performance_criteria
        self.score = score
        self.reasons = reasons

class ActionPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    improvement = db.Column(db.Text)
    who = db.Column(db.String(300))
    when = db.Column(db.String(300))
    proposed_actions = db.Column(db.Text)

    def __init__(self, improvement, who, when, proposed_actions):
        self.improvement = improvement
        self.who = who
        self.when = when
        self.proposed_actions = proposed_actions