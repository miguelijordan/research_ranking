from research_ranking import app
from research_ranking import db
from research_ranking.models import Author, Alias, DigitalBibliography, Profile, PublicationVenue, PublicationType, Publication, AuthorPublicationLink
from  research_ranking import api_db

import os


if __name__ == '__main__':
    if os.path.isfile('research_ranking/research_ranking.db'):
        os.remove('research_ranking/research_ranking.db')

    db.create_all()

    # TEST DATA
    a1 = api_db.create_author(name="José Miguel Horcas")
    a2 = api_db.create_author(name="Mónica Pinto")
    a3 = api_db.create_author(name="Lidia Fuentes")
    digital_bibliography = api_db.create_digital_bibliography(name="DBLP", url="https://dblp.uni-trier.de/")

    app.run(host='0.0.0.0', port=5555)
#
#     alias1 = api_db.create_alias(alias="Josemi", author=a1)
#
#     #
#     # newA = Author(name="Jose Miguel Horcas")
#     # newA2 = Author(name="Mónica Pinto")
#     # newAlias = Alias(alias="Josemi", author=newA)
#     # db.session.add(newA)
#     # db.session.add(newA2)
#     # db.session.add(newAlias)
#     # db.session.commit()
#
#     authors = api_db.get_authors()
#     for a in authors:
#         print(a)
#
#     #
#     # aliases = Alias.query.all()
#     # for a in aliases:
#     #     print(a)
#
#     digital_bibliography = api_db.create_digital_bibliography(name="DBLP", url="https://dblp.uni-trier.de/")
#     #
#     # newDB = DigitalBibliography(name="DBLP", url="https://dblp.uni-trier.de/")
#     # db.session.add(newDB)
#     # db.session.commit()
#
#     dbs = api_db.get_digital_bibliographies()
#     for a in dbs:
#         print(a)
#
#     newProfile = Profile(url="JosemiURL", author=newA, digital_bibliography=newDB)
#     db.session.add(newProfile)
#     db.session.commit()
#
#     profiles = Profile.query.all()
#     for a in profiles:
#         print(a)
#
# #########################################################################################
#     venue = PublicationVenue(name="Information & Software Technology", acronym="IST")
#     pub = Publication(title="title of pub", year=2019, doi="doi/midoi", type=PublicationType.JOURNAL, publication_venue=venue)
#
#     db.session.add(venue)
#     db.session.add(pub)
#     db.session.commit()
#
#     pubs = Publication.query.all()
#     for a in pubs:
#         print(a)
#
#     ##################################
#     aplink = AuthorPublicationLink(order=1, publication=pub, author=newA)
#     aplink2 = AuthorPublicationLink(order=2, publication=pub, author=newA2)
#     db.session.add(aplink)
#     db.session.add(aplink2)
#     db.session.commit()
#     # db.session.add(aplink)
#     # db.session.commit()
#     #
#     # aplink.publication(pub)
#     # newA.publications.append(pub)
#     #
#     #
#     #
#     print("-------------------")
#     for assoc in pub.authors:
#         print(assoc.author)
#         print(assoc.order)
