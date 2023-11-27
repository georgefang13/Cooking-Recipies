from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(512), nullable=False)
    text = db.Column(db.String(512), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)