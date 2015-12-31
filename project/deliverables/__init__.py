__author__ = 'afidegnum'

from flask import Blueprint
deliverables = Blueprint('deliverables', __name__)


# line added by: takwas
from . import views
