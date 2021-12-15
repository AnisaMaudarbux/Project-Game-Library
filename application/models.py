from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    dev = db.Column(db.String(100))
    genre = db.Column(db.Text(100))
    hours = db.Column(db.Integer)
    service = db.Column(db.String, db.ForeignKey('platform.service'))

class Platform(db.Model):
    platform_id = db.Column(db.Integer, primary_key = True)
    service = db.Column(db.Text(25))
    connection = db.relationship('Game', backref = 'platform')