from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Salted and encrypted password
    name = db.Column(db.String(50), nullable=False)
    recipes = db.relationship('Recipe', back_populate='user', lazy=True)
    photos = db.relationship('Photo', back_populate='user', lazy=True)
    ratings = db.relationship('Rating', back_populate='user', lazy=True)
    bookmarks = db.relationship('Bookmark', back_populate='user', lazy=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    cooking_time = db.Column(db.String(50))  # might want better type for time
    ingredients = db.relationship('QuantifiedIngredient', back_populate='recipe', lazy=True)
    steps = db.relationship('Step', back_populate='recipe', lazy=True)
    ratings = db.relationship('Rating', back_populate='recipe', lazy=True)
    bookmarks = db.relationship('Bookmark', back_populate='recipe', lazy=True)
    photos = db.relationship('Photo', back_populate='recipe', lazy=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantified_ingredients = db.relationship('QuantifiedIngredient', back_populate='ingredient', lazy=True)

class QuantifiedIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)  # might want to use a more specific type
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_extension = db.Column(db.String(8), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
