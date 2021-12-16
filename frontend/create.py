from flask_sqlalchemy import SQLAlchemy
from application import db
from application.models import  Engine, Game

db.drop_all()
db.create_all()

game = Game(name='Rayman', platform='PC')
db.session.add(game)
db.session.commit()

thing = Engine(platform = 'PC', platform_id = '1') #Add example to countries table
db.session.add(thing)
db.session.commit()

print (f"Game is {game.name}, console played on, {thing.platform}") 