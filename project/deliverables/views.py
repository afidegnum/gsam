import json
from . import deliverables
import datetime
from flask import flash, render_template, request, url_for, redirect, make_response
from flask.views import MethodView
from werkzeug.utils import secure_filename
from . forms import SectorForm, ProjectForm, BeneficiaryForm, RegionForm
from project import db
from project.deliverables.models import Sector, Project, Beneficiary
from project.location.models import Region, District
from project.media.models import Media


@deliverables.route('/sectors', methods=['GET', 'POST'])
def sectors():
    form = RegionForm(request.form)
    form.regions.choices = [('', '--- Select One ---')] + [
        (x['region'], x['regions.id']) for x in db.session.query(Region)]
    chosen_region = None
    chosen_district = None
    chosen_subdistrict = None
    chosen_village = None
    if request.method == 'POST':
        chosen_region = form.regions.data
        chosen_district = form.districts.data
        chosen_subdistrict = form.subdistricts.data
        chosen_village = form.villages.data

    context = {
        'form': form,
        'chosen_region':chosen_region,
        'chosen_district':chosen_district,
        'chosen_subdistrict':chosen_subdistrict,
        'chosen_village': chosen_village
    }
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
    return render_template('front/sectors.html', sectors=sects, sform=sform, form=form)

class DistrictAPI(MethodView):
    def get(self, reg_id):
        data = [(x['district_id'], x['district'] for x in db.session.query(District)) if x['region_id'] == reg_id]
        response = make_response(json.dump(data))
        response.content_type = 'application/json'
        return response

@deliverables.route('/')
def deliv_index():
    deliverables  = [name for name, in db.session.query(Project.title)]
    return render_template('front/deliverables.html', deliverables=deliverables)


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@deliverables.route('/add', methods=['GET', 'POST'])
def deliverables_add():
    forms = ProjectForm()
    if forms.validate_on_submit():
        pmodel = Project(title=forms.title.data, description=forms.description.data, baseline=forms.baseline.data, performance_indicator=forms.performance_indicator.data,
                         budget=forms.budget.data, author='mainuser', posted_date=datetime.datetime.utcnow(), start_date=forms.started.data, est_completion=forms.estimated_completion.data,
                         sector=forms.sector.data ,region=forms.regions.data, district=forms.district.data, subdistrict=forms.subdistrict.data, village=forms.village.data,mark_complete=False)
        media = request.files['media_gallery']
        if media and allowed_file(media.filename):
            files = secure_filename(media.filename)
            return media.save(files)
        media = Media()
        pmodel.media.append(media)
        db.session.add(pmodel)
        db.session.commit()
    return render_template('ginn/deliverables_add.html', forms=forms)


@deliverables.route('/beneficiaries')
def beneficiaries():
    return render_template('front/beneficiaries.html')

@deliverables.route('/beneficiaries/add', methods=['GET', 'POST'])
def beneficiaries_add():
    forms = BeneficiaryForm()
    if forms.validate_on_submit():
        bmodel = Beneficiary(name=forms.name.data, description=forms.descripiton.data, region=forms.regions.data, district=forms.district.data, subdistrict=forms.subdistrict.data, village=forms.village.data)
        media = request.files['media_gallery']
        if media and allowed_file(media.filename):
            files = secure_filename(media)
            media.save(files)
        bmedia = Media()
        bmodel.media.append(bmedia)
        db.session.add(bmodel)
        db.session.commit()
    return render_template('front/beneficiaries_add.html', forms=forms)
