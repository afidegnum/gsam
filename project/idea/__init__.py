__author__ = 'afidegnum'

from flask import Blueprint
idea = Blueprint('idea', __name__)


# line added by: takwas
from . import views