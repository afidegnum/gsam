# project/__init__.py


#################
#### imports ####
#################

import os
from flask.ext.bcrypt import Bcrypt
from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy



################
#### config ####
################

import config
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
bcrypt = Bcrypt(app)


####################
#### extensions ####
####################
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap(app)
db = SQLAlchemy(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
pas = os.path.join(APP_ROOT, 'static/uploads/')


###################
### blueprints ####
###################

#from project.user.views import user
from project.user import user
from project.location import location
from project.crc import crc
from project.deliverables import deliverables
from project.deliverables import views
from project.csc import csc
from project.idea import idea
from project.media import media
#from project.main.views import main_blueprint
app.register_blueprint(user, url_prefix='/account')
app.register_blueprint(csc, url_prefix='/csc')
app.register_blueprint(location)
app.register_blueprint(crc)
app.register_blueprint(media)
app.register_blueprint(deliverables, url_prefix='/deliverables')
app.add_url_rule('/dist/<int:region_id>/', view_func=views.DistrictAPI.as_view('district_api'), methods=['GET'])
app.add_url_rule('/subd/<int:dist_id>/', view_func=views.SubDistAPI.as_view('subdist_api'), methods=['GET'])
app.add_url_rule('/vill/<int:subd_id>/', view_func=views.VillageAPI.as_view('village_api'), methods=['GET'])



###################
### flask-login ####
###################



login_manager.login_view = "user.login"
login_manager.login_message_category = 'danger'


########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500