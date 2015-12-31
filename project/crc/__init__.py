from flask import Blueprint
crcard = Blueprint('crcard', __name__)


# line added by: takwas
from . import views
