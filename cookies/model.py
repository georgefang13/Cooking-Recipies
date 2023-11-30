from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Store salted and encrypted password
    name = db.Column(db.String(64), nullable=False)

    # # One-to-Many relationship between users and recipes
    recipes = db.relationship('Recipe', back_populates='user', lazy=True)

    # # One-to-Many relationship between users and ratings
    # ratings = db.relationship('Rating', back_populates='user', lazy=True)

    # # One-to-Many relationship between users and bookmarks
    # bookmarks = db.relationship('Bookmark', back_populates='user', lazy=True)

    # # One-to-Many relationship between users and photos
    # photos = db.relationship('Photo', back_populates='user', lazy=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    person_count = db.Column(db.Integer, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)

    # # Many-to-One relationship between recipes and users
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='recipes')


    # # One-to-Many relationship between recipes and quantified ingredients
    # quantified_ingredients = db.relationship('QuantifiedIngredient', back_populates='recipe', lazy=True)

    # # One-to-Many relationship between recipes and steps
    # steps = db.relationship('Step', back_populates='recipe', lazy=True)

    # # One-to-Many relationship between recipes and ratings
    # ratings = db.relationship('Rating', back_populates='recipe', lazy=True)

    # # One-to-Many relationship between recipes and bookmarks
    # bookmarks = db.relationship('Bookmark', back_populates='recipe', lazy=True)

    # # One-to-Many relationship between recipes and photos
    # photos = db.relationship('Photo', back_populates='recipe', lazy=True)

# class Ingredient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

#     # One-to-Many relationship between ingredients and quantified ingredients
#     quantified_ingredients = db.relationship('QuantifiedIngredient', back_populates='ingredient', lazy=True)

# class QuantifiedIngredient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.String(20), nullable=False)

#     # Many-to-One relationship between quantified ingredients and recipes
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

#     # Many-to-One relationship between quantified ingredients and ingredients
#     ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)

# class Step(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#     sequence_number = db.Column(db.Integer, nullable=False)

#     # Many-to-One relationship between steps and recipes
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

# class Rating(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     value = db.Column(db.Integer, nullable=False)

#     # Many-to-One relationship between ratings and users
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     # Many-to-One relationship between ratings and recipes
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

# class Bookmark(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     # Many-to-One relationship between bookmarks and users
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     # Many-to-One relationship between bookmarks and recipes
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

# class Photo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     file_extension = db.Column(db.String(10), nullable=True)

#     # Many-to-One relationship between photos and users
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     # Many-to-One relationship between photos and recipes
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)










#### Uncomment this for the hardcoded boilerplate we initially used
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     name = db.Column(db.String(64), nullable=False)

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user = db.Column(db.String(512), nullable=False)
#     text = db.Column(db.String(512), nullable=False)
#     timestamp = db.Column(db.DateTime(), nullable=False)




# from . import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False) # max length of 128 characters, forbidden to have null value
#     name = db.Column(db.String(64), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     messages = db.relationship('Message', back_populates='user')

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key matches the primary key of the user table
#     user = db.relationship('User', back_populates='messages')
#     text = db.Column(db.String(512), nullable=False)
#     timestamp = db.Column(db.DateTime(), nullable=False)
#     response_to_id = db.Column(db.Integer, db.ForeignKey('message.id')) # if null, its an original message, otherwese its a response
#     response_to = db.relationship('Message', back_populates='responses', remote_side=[id]) # the message which this message is responding to, if null, its original
#     responses = db.relationship('Message', back_populates='response_to', remote_side=[response_to_id]) # list of response messages to this message, if empty, no responses