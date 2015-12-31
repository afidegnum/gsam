
from . import deliverables
import datetime
from flask import flash, render_template, request, url_for, redirect
from . forms import SectorForm, ProjectForm, BeneficiaryForm
from project import db
from project.deliverables.models import Sector, Project, Beneficiary


@deliverables.route('/sectors', methods=['GET', 'POST'])
def sectors():
    sform = SectorForm()
    sects = [name for name, in db.session.query(Sector.name)]
    if request.method == 'POST'and sform.validate_on_submit():
        sector = Sector(name=sform.name.data)
        db.session.add(sector)
        db.session.commit()
        flash(message='sector successfully added')
        return redirect(url_for('deliverables.sectors'))
    elif request.method == 'GET':
        sects = [name for name, in db.session.query(Sector.name)]
    return render_template('front/sectors.html', sectors=sects, form=sform)

@deliverables.route('/beneficiaries')
def beneficiaries():
    return render_template('front/beneficiaries.html')


@deliverables.route('/')
def deliv_index():
    deliverables  = [name for name, in db.session.query(Project.title)]
    return render_template('front/deliverables.html', deliverables=deliverables)

@deliverables.route('/add', methods=['GET', 'POST'])
def deliverables():
    forms = ProjectForm()
    if request.method == 'POST' and forms.validate_on_submit():
        pmodel = Project(title=forms.title.data, description=forms.description.data, baseline=forms.baseline.data, performance_indicator=forms.performance_indicator.data, budget=forms.budget.data, author='mainuser', posted_date=datetime.datetime.utcnow(), start_date=forms.started.data, est_completion=forms.estimated_completion.data, mark_complete=forms.completed.data)
        db.session.add(pmodel)
        db.session.commit()
    return render_template('front/deliverables_edit.html', forms=forms)


