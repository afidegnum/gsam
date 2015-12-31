#!/home/afidegnum/gsam/bin/python

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import db, app
from project.models import Role
from project.deliverables.models import Sector

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_them():
    db.create_all()
    return "New Tables are created!"


@manager.command
def wipe_them():
    db.drop_all()
    return "Oooo! They've Gone"


@manager.command
def add_roles(name):
    name = Role(name=name, front='Y')
    db.session.add(name)
    db.session.commit()
    names = [name for name, in db.session.query(Role.name).all()]
    return names

@manager.command
def del_roles(name):
    name = Role(name=name)
    db.session.delete(name)
    db.session.commit()
    names = [name for name, in db.session.query(Role.name).all()]
    return names

@manager.command
def add_sectors(name):
    name = Sector(name=name)
    db.session.add(name)
    db.session.commit()
    sectors = [name for name, in db.session.query(Sector.name).all()]
    return sectors





if __name__ == '__main__':
    manager.run()
