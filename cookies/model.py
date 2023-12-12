from . import db
import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Store salted and encrypted password
    name = db.Column(db.String(64), nullable=False)

    # # One-to-Many relationship between users and recipes
    recipes = db.relationship('Recipe', back_populates='user')

    # One-to-Many relationship between users and ratings
    ratings = db.relationship('Rating', back_populates='user')

    # One-to-Many relationship between users and bookmarks
    bookmarks = db.relationship('Bookmark', back_populates='user')

    # One-to-Many relationship between users and photos
    photos = db.relationship('Photo', back_populates='user')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    person_count = db.Column(db.Integer, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)

    # Many-to-One relationship between recipes and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='recipes')


    # One-to-Many relationship between recipes and quantified ingredients
    quantified_ingredients = db.relationship('QuantifiedIngredient', back_populates='recipe')

    # One-to-Many relationship between recipes and steps
    steps = db.relationship('Step', back_populates='recipe')

    # One-to-Many relationship between recipes and ratings
    ratings = db.relationship('Rating', back_populates='recipe')

    # One-to-Many relationship between recipes and bookmarks
    bookmarks = db.relationship('Bookmark', back_populates='recipe')

    # One-to-Many relationship between recipes and photos
    photos = db.relationship('Photo', back_populates='recipe')

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # One-to-Many relationship between ingredients and quantified ingredients
    quantified_ingredients = db.relationship('QuantifiedIngredient', back_populates='ingredient')

class QuantifiedIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    units = db.Column(db.String(20), nullable=False)

    # Many-to-One relationship between quantified ingredients and recipes
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='quantified_ingredients')

    # Many-to-One relationship between quantified ingredients and ingredients
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    ingredient = db.relationship('Ingredient', back_populates='quantified_ingredients')

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    sequence_number = db.Column(db.Integer, nullable=False)

    # Many-to-One relationship between steps and recipes
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='steps')

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)

    # Many-to-One relationship between ratings and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='ratings')

    # Many-to-One relationship between ratings and recipes
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ratings')

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Many-to-One relationship between bookmarks and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='bookmarks')

    # # Many-to-One relationship between bookmarks and recipes
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='bookmarks')

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_extension = db.Column(db.String(10), nullable=True)

    # Many-to-One relationship between photos and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='photos')

    # Many-to-One relationship between photos and recipes
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='photos')