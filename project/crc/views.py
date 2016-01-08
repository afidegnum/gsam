import datetime
from flask import render_template
from . import crc
from project import db
from project.crc.forms import CrCForm, BasicQuestionForm
from project.crc.models import CrC, BasicQuestion


@crc.route('/')
def crcards():
    return render_template('front/crcards.html')


@crc.route('/add')
def add_crc():
    cform = CrCForm()
    if cform.validate_on_submit():
        crcard = CrC(title =cform.title.data, description=cform.description.data, service_target=cform.service_target, service_aspect=cform.service_aspect.data, author='',date=datetime.datetime.utcnow(), purpose_of_study=cform.purpose_of_study.data)
        db.session.add(crcard)
        db.session.commit()
    return render_template('front/add_crc.html', forms=cform)


@crc.route('/questions')
def questions():
    return render_template('front/questions.html')


@crc.route('/questions/add')
def add_questions():
    return render_template('front/add_questions.html')


@crc.route('/aspects')
def aspects():
    return render_template('front/aspects.html')


@crc.route('/aspects/add')
def add_aspect():
    return render_template('front/add_aspects.html')


@crc.route('/answers')
def answers():
    return render_template('front/answers.html')


@crc.route('/answers/add')
def add_answer():
    return render_template('front/add_answer.html')
