from application import db 
from application.models import  Platform

db.create_all()

Rayman = Platform(service = 'PC') #Add example to countries table
Pokemon_X= Platform(service = '2DS')
db.session.add(Rayman)
db.session.add(Pokemon_X)
db.session.commit()