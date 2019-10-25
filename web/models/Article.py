from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prix = db.Column(db.String(100))
    titre = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))
    location = db.Column(db.String(100))
    