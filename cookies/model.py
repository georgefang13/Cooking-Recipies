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

#implement with JSON
class Recipe(db.Model):
    form_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(512), nullable=False)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
#different class model, which has a relationship
#ingredients = db.Column(db.Table)
    
    
    #description, ingredients, steps, image
