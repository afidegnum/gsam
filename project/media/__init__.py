__author__ = 'afidegnum'

from flask import Blueprint
media = Blueprint('media', __name__)


# line added by: takwas
from . import views
