from . import ranking
from flask import render_template

@ranking.route('/')
@ranking.route('/home')
@ranking.route('/ranking')
def home():
    return render_template('ranking/ranking.html')
