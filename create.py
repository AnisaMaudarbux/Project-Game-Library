from application import db 
from application.models import  Engine, Game

db.drop_all()
db.create_all()

Rayman = Engine(platform = 'PC') #Add example to countries table
Pokemon_X= Engine(platform = '2DS')
db.session.add(Rayman)
db.session.add(Pokemon_X)
db.session.commit()