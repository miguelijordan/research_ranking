from . import db
import enum

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    aliases = db.relationship('Alias', backref='author', lazy=True)
    profiles = db.relationship('Profile', backref='author', lazy=True)
    publications = db.relationship('AuthorPublicationLink', back_populates="author")

    def __repr__(self):
        return '<Author %r>' % self.name

class Alias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return '<Alias %r>' % self.alias

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    digital_bibliography_id = db.Column(db.Integer, db.ForeignKey('digital_bibliography.id'), nullable=False)

    def __repr__(self):
        return '<Profile %r (%r)>' % (self.url, self.digital_bibliography)
#
class DigitalBibliography(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    url = db.Column(db.String(100), nullable=False, unique=True)
    profiles = db.relationship('Profile', backref='digital_bibliography', lazy=True)

    def __repr__(self):
        return '<DigitalBibliography %r, %r>' % (self.name, self.url)

class PublicationType(enum.Enum):
    JOURNAL = "Journal Article"
    CONFERENCE = "Conference"
    OTHER = "Others"

class PublicationVenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    acronym = db.Column(db.String(25), nullable=True)
    publications = db.relationship('Publication', backref='publication_venue', lazy=True)

    def __repr__(self):
        return '<PublicatonVenue %r (%r)>' % (self.name, self.acronym)

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    doi = db.Column(db.String(100), unique=True)
    type = db.Column(db.Enum(PublicationType), nullable=False)
    publication_venue_id = db.Column(db.Integer, db.ForeignKey('publication_venue.id'), nullable=False)
    authors = db.relationship('AuthorPublicationLink', back_populates="publication")

    def __repr__(self):
        return '<Publication %r. %r. %r. %r. %r)>' % (self.title, self.year, self.doi, self.type, self.publication_venue)

class AuthorPublicationLink(db.Model):
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    publication = db.relationship("Publication", back_populates="authors")
    author = db.relationship("Author", back_populates="publications")
