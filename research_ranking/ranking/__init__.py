from flask import Blueprint

ranking = Blueprint('ranking', __name__,
                    template_folder='templates',
                    static_folder='static')

from . import views
