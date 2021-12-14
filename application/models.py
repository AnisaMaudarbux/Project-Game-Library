from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    publ = db.Column(db.String(100))
    genre = db.Column(db.Text(100))
    hour = db.Column(db.Integer)