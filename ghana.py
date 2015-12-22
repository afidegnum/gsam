#!/home/afidegnum/gsam/bin/python

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import db, app
from project.models import Role

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
def add_roles(name='name'):
    name = Role(name)
    name.db.session.add(name)
    name.db.session.commit()


@manager.command
def del_roles():
    name = Role(name='name')
    name.db.session.delete(name)
    name.db.session.commit()


if __name__ == '__main__':
    manager.run()
