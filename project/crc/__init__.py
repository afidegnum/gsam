from flask import Blueprint
crc = Blueprint('crc', __name__)


# line added by: takwas
from . import views
