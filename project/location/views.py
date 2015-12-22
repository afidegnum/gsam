from flask import render_template, jsonify
from project import db, location
from project.location.models import Region, District, Subdistrict, Village


@location.route('/regions')
def regions():
    names = [name for name, in db.session.query(Region.name).all()]
    return render_template('regions.html', names=names)
    pass

@location.route('/districts')
def districts():
    names = [name for name, in db.session.query(District.name).all()]
    return render_template('roles.html', names=names)
    pass

@location.route('/subdistricts')
def subdistricts():
    names = [name for name, in db.session.query(Subdistrict.name).all()]
    return render_template('roles.html', names=names)
    pass

@location.route('villages')
def villages():
    names = [name for name, in db.session.query(Village.name).all()]
    return render_template('roles.html', names=names)
    pass



