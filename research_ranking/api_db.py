from .models import db, Author, Alias, DigitalBibliography, Profile, PublicationVenue, PublicationType, Publication, AuthorPublicationLink

# CREATE operations
def create_author(name: str):
    object = Author(name=name)
    db.session.add(object)
    db.session.commit()
    return object

def create_alias(alias: str, author: Author):
    object = Alias(alias=alias, author=author)
    db.session.add(object)
    db.session.commit()
    return object

def create_digital_bibliography(name: str, url: str):
    object = DigitalBibliography(name=name, url=url)
    db.session.add(object)
    db.session.commit()
    return object

def create_profile(url: str, author: Author, digital_bibliography: DigitalBibliography):
    object = Profile(url=url, author=author, digital_bibliography=digital_bibliography)
    db.session.add(object)
    db.session.commit()
    return object

def create_publication_venue(name: str, acronym: str = None):
    object = PublicationVenue(name=name, acronym=acronym)
    db.session.add(object)
    db.session.commit()
    return object

def create_publication(title: str, year: int, doi: str, type: PublicationType, publication_venue: PublicationVenue, authors: list):
    object = Publication(title=title, year=year, doi=doi, type=type, publication_venue=publication_venue)
    db.session.add(object)
    # Add authors of publication
    order = 1
    for a in authors:
        assoc = AuthorPublicationLink(order=order, publication=object, author=a)
        db.session.add(assoc)
        order += 1
    db.session.commit()
    return object

# READ operations
def get_authors():
    return Author.query.all()

def get_author(name_or_alias: str) -> Author:
    author = Author.query.filter_by(name=name_or_alias).first()
    if not author:
        alias = Alias.query.filter_by(alias=name_or_alias).first()
        if alias:
            author = alias.author
    return author

def get_digital_bibliographies():
    return DigitalBibliography.query.all()

def get_publication_venue(name: str) -> PublicationVenue:
    return PublicationVenue.query.filter_by(name=name).first()

# UPDATE operations

# DELETE operations
