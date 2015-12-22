from project import db

class Region(db.Model):
    __tablename__ = 'regions'
    region = db.Column(db.String(30))
    id = db.Column(db.Integer, primary_key=True)
    districts = db.relationship("District", backref='regions')

    def __init__(self, region):
        self.region = region

class District(db.Model):
    __tablename__ = 'districts'
    district = db.Column(db.String(90))
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    subdistricts = db.relationship("Subdistrict", backref='districts')

    def __init__(self, id, region_id):
        self.id = id
        self.region_id = region_id

class Subdistrict(db.Model):
    __tablename__ = 'subdistricts'
    id = db.Column(db.Integer, primary_key=True)
    subdistrict = db.Column(db.String(50))
    districts = db.Column(db.Integer, db.ForeignKey('districts.id'))
    villages = db.relationship("Village", backref='subdistricts')


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


    def __init__(self, village, lattitude, longitude, subdistrict_id):
        self.village = village
        self.lattitude = lattitude
        self.longitude = longitude
        self.subdistrict_id = subdistrict_id








