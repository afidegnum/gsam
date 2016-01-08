__author__ = 'afidegnum'

from flask import Blueprint
csc = Blueprint('csc', __name__)


# line added by: takwas
from . import views