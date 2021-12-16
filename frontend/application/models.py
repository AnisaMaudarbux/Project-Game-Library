from flask_sqlalchemy import SQLAlchemy
from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    dev = db.Column(db.String(100))
    genre = db.Column(db.Text(100))
    hours = db.Column(db.Integer)
    platform = db.Column(db.Text, db.ForeignKey('engine.platform'))

class Engine(db.Model):
    platform_id = db.Column(db.Integer, primary_key = True)
    platform = db.Column(db.String(25))
    Connection = db.relationship('Game', backref = 'engine')