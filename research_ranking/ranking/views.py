from . import ranking
from .. import db, api_db
from ..models import Author, PublicationType, DigitalBibliography
from flask import render_template, request
import ast
from ..libs import dblp_search


def get_publication_type_from_dblp(type: str) -> PublicationType:
    if type == "Journal Articles":
        return PublicationType.JOURNAL
    elif type == "Conference and Workshop Papers":
        return PublicationType.CONFERENCE
    else:
        return PublicationType.OTHER

def sortAuthors(author):
    return author['n_publications']

def get_ranking():
    ranking = []
    authors = Author.query.all()
    for a in authors:
        author = dict()
        author['name'] = a.name
        author['n_publications'] = len(a.publications)
        author['n_journals'] = len([p for p in a.publications if p.publication.type==PublicationType.JOURNAL])
        author['n_conferences'] = len([p for p in a.publications if p.publication.type==PublicationType.CONFERENCE])
        author['n_others'] = len([p for p in a.publications if p.publication.type==PublicationType.OTHER])
        ranking.append(author)
    ranking.sort(key=sortAuthors, reverse=True)
    return ranking

@ranking.route('/')
@ranking.route('/home')
@ranking.route('/ranking', methods=['GET', 'POST'])
def home():
    authors = None

    if request.method == 'POST':
        if 'search_button' in request.form:
            query = request.form['query']
            authors = dblp_search.search_author(query)

        elif 'add_button' in request.form:
            authors = request.form.getlist('author')
            digital_bibliography = DigitalBibliography.query.filter_by(id=request.form['DigitalBibliography']).first()
            for a in authors:
                a = ast.literal_eval(a)
                newAuthor = api_db.get_author(name_or_alias=a['name'])
                if not newAuthor:
                    newAuthor = api_db.create_author(name=a['name'])
                    api_db.create_alias(alias=a['alias'], author=newAuthor)
                    api_db.create_profile(url=a['url'], author=newAuthor, digital_bibliography=digital_bibliography)
                    publications = dblp_search.get_publications(newAuthor.name)
                    for p in publications:
                        coauthors = []
                        for coauthor in p['authors']:
                            newCoauthor = api_db.get_author(name_or_alias=coauthor)
                            if not newCoauthor:
                                newCoauthor = api_db.create_author(name=coauthor)
                            coauthors.append(newCoauthor)

                        venue = api_db.get_publication_venue(name=p['venue'])
                        if not venue:
                            venue = api_db.create_publication_venue(name=p['venue'], acronym=p['venue'])
                        api_db.create_publication(title=p['title'], year=p['year'], doi=p['doi'], type=get_publication_type_from_dblp(p['type']), publication_venue=venue, authors=coauthors)

    ranking = get_ranking()
    dbs = DigitalBibliography.query.all()

    return render_template('home.html', ranking=ranking, digital_bibliographies=dbs, authors=authors)
