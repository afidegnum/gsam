import datetime
from flask import render_template, flash, redirect, url_for, g, request

# line modified by: takwas
import flask
from project import db, login_manager, bcrypt

# line added by: takwas
from . import user as user_blueprint

#from project.user import user
from project.models import Role, User
from project.user.forms import RegisterForm, LoginForm
from flask.ext.login import login_user, logout_user, login_required, session, current_user


# print "B:UEPPPP!! {}".format(user_blueprint)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@user_blueprint.before_request
def get_current_user():
    g.user = current_user

# line modified by: takwas
@user_blueprint.route('/roles/')
def roles():
    names = [name for name, in db.session.query(Role.name).all()]
    return render_template('front/roles.html', names=names)

@user_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def members():
    user = 'Hi {}'.format(g.user.username)
    return render_template("gstheme/members.html", user = user)

# line modified by: takwas
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if g.user.is_authenticated:
        flash("You are already Logged in", 'warning')
        return redirect(request.args.get('next') or url_for('user.members'))
    form = RegisterForm()
    if form.validate_on_submit():
        users = User(username=form.username.data,
                    title=form.title.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    other_name=form.other_names.data,
                    password = form.password.data,
                    phone=form.phone.data,
                    email=form.email.data,
                    address=form.address.data,
                    region=form.regions.data.id,
                    district=form.district.data.id,
                    subdistrict=form.subdistrict.data.id,
                    village=form.village.data.id,
                    role=form.roles.data.id,
                    activation='',
                    active=True,
                    created_date=datetime.datetime.utcnow(),
                    last_login=datetime.datetime.utcnow(),
                    retries=0,
                    picture="Default")
        db.session.add(users)
        db.session.commit()
        usr = User.query.filter_by(username=form.username.data).first()
        flash('Thank you for registering, Continue from your account', 'success')
        login_user(usr)
        return redirect(url_for("user.members"))
    return render_template("gstheme/register.html", rform=form)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if g.user.is_authenticated:
        flash("You are already Logged in", 'warning')
        return redirect(request.args.get('next') or url_for('members'))
    error = ""
    lforms = LoginForm()
    if lforms.validate_on_submit():
        user = User.query.filter_by(username=lforms.username.data).first()
        if user is not None and bcrypt.check_password_hash(user.password, lforms.password.data):
            login_user(user, remember=lforms.remember.data)
            flash('You are sucessfuly Logged in', 'success')
            return redirect(url_for('members'))
        else:
            flash("You have entered an incorrect username and passwor", "danger")
    return render_template("gstheme/login.html", forms=lforms, error=error)


@user_blueprint.route("/activate", methods=['GET', 'POST'])
@login_required
def activate():
    return render_template("front/activate.html")