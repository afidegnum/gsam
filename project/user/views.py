from flask import render_template
from project import db, user
#from project.user import user
from project.models import Role, User
from project.user.forms import RegisterForm




@user.route('/roles/')
def roles():
    # names = [name for name, in db.session.query(Role.name).all()]
    names = "Wlecome to Gsam"
    return render_template('front/roles.html', names=names)

@user.route('/register')
def register():
    form = RegisterForm()
    user = User(username=form.username.data, title=form.title.data, first_name=form.first_name.data, last_name=form.last_name.data, other_name=form.other_names.data, password=form.password.data, phone=form.phone.data, email=form.email.data, address=form.address.data)
    return render_template('front/register.html', form = form)
