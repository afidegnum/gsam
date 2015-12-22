__author__ = 'afidegnum'

from flask import Blueprint
user = Blueprint('user', __name__)


# line added by: takwas
from . import views
