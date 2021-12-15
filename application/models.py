from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    publ = db.Column(db.String(100))
    genre = db.Column(db.Text(100))
    hours = db.Column(db.Integer)

