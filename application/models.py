from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    dev = db.Column(db.String(100))
    genre = db.Column(db.Text(100))
    hours = db.Column(db.Integer)
    service = db.Column(db.String, db.ForeignKey('platform.service'))

class Platform(db.Model):
    service = db.Column(db.String(20), primary_key = True)
    connection = db.relationship('Game', backref = 'platform')