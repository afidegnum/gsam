
import datetime
from flask import render_template, request
from project import db
from project.csc.forms import CSForm, CsCommunityform, KeyLeadersForm, AgendaForm, CSInputform, CSPerformanceForm, \
    SelfEvaluationForm, ActionPlanForm
from project.csc.models import CSC, CSCommunity, KeyLeader, Agenda, CSinput, CSPerformance, SelfEvaluation, ActionPlan
from werkzeug.utils import secure_filename
from project.deliverables.views import ALLOWED_EXTENSIONS, allowed_file


__author__ = 'afidegnum'
from . import csc

@csc.route('/', methods=['GET', 'POST'])
def score_cards():
    return render_template('front/score_cards.html')

@csc.route('/add', methods=['GET', 'POST'])
def score_add():
    sforms = CSForm()
    if sforms.validate_on_submit():
        cscard = CSC(name=sforms.name.data, description=sforms.description.data, sector=sforms.sector.data, age_from=sforms.age_from.data, age_to=sforms.age_to.data, income_from=sforms.income_from.data, income_to=sforms.income_to.data, budget=sforms.budget.data, date=datetime.datetime.utcnow())
        media = request.files['media_gallery']
        if media and allowed_file(media.filename):
            files = secure_filename(media.filename)
            media.save(files)
        cscard.media.append(media)
        db.session.add(cscard)
        db.session.commit()
    return render_template('front/csc_add.html', forms=sforms)


@csc.route('/communities', methods=['GET', 'POST'])
def communities():
    return render_template('front/communitites.html')

@csc.route('/communities/add')
def add_communities():
    cforms = CsCommunityform()
    if cforms.validate_on_submit():
        community = CSCommunity(name=cforms.name.data, region=cforms.regions.data, subgroup=cforms.subgroup.data, subdistrict=cforms.subdistrict.data, village=cforms.village.data)
        media = request.files['media_gallery']
        if media and allowed_file(media.filename):
            files = secure_filename(media.filename)
            media.save(files)
        community.media.append(media)
        db.session.add(community)
        db.session.commit()
    return render_template('front/add_communities.html', forms=cforms)

@csc.route('/keyleaders')
def key_leaders():
    return render_template('front/leaders.html')

@csc.route('/keyleaders/add')
def add_leaders():
    lform = KeyLeadersForm()
    if lform.validate_on_submit():
        leader = KeyLeader(name = lform.name.data, address=lform.address.data, community=lform.community.data, picture=lform.picture.data)
        db.session.add(leader)
        db.session.commit()
    return render_template('front/add_leaders.html', forms=lform)

@csc.route('/agenda')
def agenda_list():
    return render_template('front/agenda.html')

@csc.route('/agenda/add')
def add_agenda():
    aform = AgendaForm()
    if aform.validate_on_submit():
        agenda = Agenda(scard=aform.score_card.data, cscommunity=aform.community.data, meeting_date=aform.meeting_date.data, facilitator=aform.facilitators.data, notes=aform.notes.data, submit_date=datetime.datetime.utcnow())
        db.session.add(agenda)
        db.session.commit()
    return render_template('front/add_agenda.html', forms = aform)

@csc.route('/inputs')
def csc_inputs():
    return render_template('front/csc_input.html')

@csc.route('/inputs/add')
def cscinputs_add():
    iform = CSInputform()
    if iform.validate_on_submit():
        csinput = CSinput(community='', cscard='', name=iform.name.data, submit_from='', beneficiaries=iform.beneficiaries.data, indicators=iform.indicators.data, entitlements=iform.entitlements.data, actuals=iform.actuals.data, remark=iform.remark.data, input_date=datetime.datetime.utcnow())
        db.session.add(csinput)
        db.session.commit()
    return render_template('front/csinput_add.html', forms = iform)

@csc.route('/performances')
def performances():
    return render_template('front/performances.html')

@csc.route('/performances/add')
def add_performance():
    pform = CSPerformanceForm()
    if pform.validate_on_submit():
        performance = CSPerformance(name=pform.name.data, community='', cscard='', indicator=pform.indicator.data, score=pform.score.data, six_month=pform.six_month.data, year=pform.year_later.data, reasons_for_change=pform.reasons_for_change.data, submit_date=datetime.datetime.utcnow() )
        db.session.add(performance)
        db.session.commit()
    return render_template('front/add_performance.html', forms=pform)


@csc.route('/evaluations')
def evaluation():
    return render_template('front/evaluation.html')


@csc.route('/evaluations/add')
def add_evaluation():
    eform = SelfEvaluationForm()
    if eform.validate_on_submit():
        evaluate = SelfEvaluation(name=eform.name.data, community='', cscard='', performance_criteria=eform.performance_criteria.data, score=eform.score.data, reasons=eform.reasons.data, submit_date=datetime.datetime.utcnow())
        db.session.add(evaluate)
        db.session.commit()
    return render_template('front/add_evaluations.html', forms=eform)


@csc.route('actions')
def actions():
    return render_template('front/actions.html')


@csc.route('/actions/add')
def actions_add():
    aform = ActionPlanForm()
    if aform.validate_on_submit():
        action = ActionPlan(cscard='', community='', improvement=aform.improvement.data, who=aform.who.data, when=aform.when.data, proposed_actions=aform.proposed_actions.data, submit_date=datetime.datetime.utcnow())
    return render_template('front/actions_add.html', forms = aform)

