from application import db 
from application.models import  Engine, Game

db.create_all()

testgame = Engine(platform = 'PC', platform_id = '1') #Add example to countries table
db.session.add(testgame)
db.session.commit()