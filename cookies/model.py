from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False) # max length of 128 characters, forbidden to have null value
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    messages = db.relationship('Message', back_populates='user')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key matches the primary key of the user table
    user = db.relationship('User', back_populates='messages')
    text = db.Column(db.String(512), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    response_to_id = db.Column(db.Integer, db.ForeignKey('message.id')) # if null, its an original message, otherwese its a response
    response_to = db.relationship('Message', back_populates='responses', remote_side=[id]) # the message which this message is responding to, if null, its original
    responses = db.relationship('Message', back_populates='response_to', remote_side=[response_to_id]) # list of response messages to this message, if empty, no responses