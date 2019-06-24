from research_ranking import db

db.create_all()

from research_ranking.models import Author

newA = Author(name="José Miguel Horcas")
# newAlias = Alias(alias="Josemi", author=newA)
db.session.add(newA)
db.session.commit()
# from research_ranking.models import Bibliography
# dblp = Bibliography(name='DBLP', url='https://dblp.uni-trier.de/')
# db.session.add(dblp)
# db.session.commit()
