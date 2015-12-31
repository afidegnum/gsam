from flask import render_template

# line modified by: takwas
from project import db#, user

# line added by: takwas
from . import user as user_blueprint

#from project.user import user
from project.models import Role, User
from project.user.forms import RegisterForm

# print "B:UEPPPP!! {}".format(user_blueprint)


# line modified by: takwas
@user_blueprint.route('/roles/')
def roles():
    names = [name for name, in db.session.query(Role.name).all()]
    return render_template('front/roles.html', names=names)

# line modified by: takwas
@user_blueprint.route('/register/')
def register():
    form = RegisterForm()
    user = User(username=form.username.data, title=form.title.data, first_name=form.first_name.data, last_name=form.last_name.data, other_name=form.other_names.data, password=form.password.data, phone=form.phone.data, email=form.email.data, address=form.address.data)
    return render_template('front/register.html', form = form)
