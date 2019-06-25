from flask import Blueprint
# from ..models import Author

ranking = Blueprint('ranking',
                    __name__,
                    template_folder='templates',
                    static_folder='static')

from . import views
