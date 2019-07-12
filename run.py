from research_ranking import create_app
from research_ranking import db
from research_ranking.models import Author, Alias, DigitalBibliography, Profile, PublicationVenue, PublicationType, Publication, AuthorPublicationLink
from research_ranking import api_db

import os


if __name__ == '__main__':
    if os.path.isfile('research_ranking/research_ranking.db'):
        os.remove('research_ranking/research_ranking.db')

    app = create_app()
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    # TEST DATA
    db_dblp = api_db.create_digital_bibliography(name="DBLP", url="https://dblp.uni-trier.de/")
    # a1 = api_db.create_author(name="José Miguel Horcas")
    # a2 = api_db.create_author(name="Mónica Pinto")
    # a3 = api_db.create_author(name="Lidia Fuentes")
    # alias_a1 = api_db.create_alias(alias="Josemi", author=a1)
    # profile_a1 = api_db.create_profile(url="JosemiURL", author=a1, digital_bibliography=db_dblp)
    # venue = api_db.create_publication_venue(name="Information & Software Technology", acronym="IST")
    # pub1 = api_db.create_publication(title="Pub1 title", year=2017, doi="doi/pub1", type=PublicationType.JOURNAL, publication_venue=venue, authors=[a1, a2, a3])
    # pub2 = api_db.create_publication(title="Pub2 title", year=2018, doi="doi/pub2", type=PublicationType.CONFERENCE, publication_venue=venue, authors=[a1, a2])
    # pub3 = api_db.create_publication(title="Pub3 title", year=2019, doi="doi/pub3", type=PublicationType.JOURNAL, publication_venue=venue, authors=[a1])

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
