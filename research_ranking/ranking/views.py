from . import ranking
from flask import render_template
# from ..models import Author

@ranking.route('/')
@ranking.route('/home')
@ranking.route('/ranking')
def home():
    # authors = api_db.get_authors()
    authors = Author.query.all()
    return render_template('ranking/ranking.html', authors=authors)
