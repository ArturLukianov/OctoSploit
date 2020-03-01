from app import db


class Sploit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    name = db.Column(db.String(255))


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(11))
