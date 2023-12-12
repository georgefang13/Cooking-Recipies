import datetime
from os import abort
import dateutil.tz
from flask import Blueprint, render_template, render_template, request, redirect, url_for, flash, current_app
import flask_login
from flask_login import current_user
from .model import User, Recipe, QuantifiedIngredient, Step, Ingredient, Bookmark, Rating
from pathlib import Path

from . import db
from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    recipes = Recipe.query.all()
    return render_template("main/index.html", posts=recipes)

@bp.route('/profile/<int:user_id>')
def profile(user_id):
    # Query for the user based on the user_id
    user = User.query.filter_by(id=user_id).one()

    # Access all recipes for the user using the relationship attribute
    recipes = list(user.recipes)
    return render_template('main/profile.html', user=user, posts=recipes)

#controller for accessing a user's bookmarked recipes
@bp.route("/bookmark/<int:recipe_id>", methods=['POST'])
@flask_login.login_required
def bookmark(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    user = flask_login.current_user
    bookmark = Bookmark(user=user, recipe=recipe)
    db.session.add(bookmark)
    db.session.commit()
    return redirect(url_for('main.recipe', recipe_id=recipe.id))

@bp.route("/unbookmark/<int:recipe_id>", methods=['POST'])
@flask_login.login_required
def unbookmark(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    user = flask_login.current_user
    # query = db.select(Bookmark).where(recipe_id == recipe.id).where(user == flask_login.current_user)
    bookmark = Bookmark.query.filter_by(user_id=user.id, recipe_id=recipe_id).first()
    if bookmark:
        db.session.delete(bookmark)
        db.session.commit()

    return redirect(url_for("main.recipe", recipe_id=recipe.id))

@bp.route("/bookmark/<int:user_id>")
def bookmark_page(user_id):
    user = User.query.filter_by(id=user_id).one()
    bookmarked = list(user.bookmarks)
    # for each bookmark in bookmarked, add bookmark.recipe to a list
    recipes = []
    for bookmark in bookmarked:
        recipes.append(bookmark.recipe)
    return render_template("main/bookmark.html", user=user, posts=recipes)

@bp.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).one()

    bookmark_button = "bookmark"  # Default state

    if current_user.is_authenticated:
        # Check if the current user has bookmarked this specific recipe
        bookmark = Bookmark.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
        if bookmark:
            bookmark_button = "bookmarked"
    return render_template('main/recipe.html', user=recipe.user, post=recipe, bookmark_button=bookmark_button)

@bp.route("/new_recipe", methods=['GET', 'POST'])
@flask_login.login_required
def new_recipe():
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.form.get('recipe-title')
        description = request.form.get('recipe-description')
        cook_time = request.form.get('cook-time')
        num_people = request.form.get('num-people')
        # timestamp = datetime.datetime.now(dateutil.tz.tzlocal())

        # Create a new recipe and link it to the current user
        recipe = Recipe(title=title, user=current_user, description=description, cooking_time=cook_time, person_count=num_people)
        recipe.user = current_user  # Set the relationship here

        # Process ingredients and quantified ingredients
        ingredient_names = request.form.getlist('ingredients[]')
        units = request.form.getlist('units[]')
        quantities = request.form.getlist('quantities[]')

        for ingredient_name, unit, quantity in zip(ingredient_names, units, quantities):
            if not ingredient_name:
                break  # No more ingredients

            # Check if the ingredient already exists
            ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ingredient_name)
                db.session.add(ingredient)
                db.session.commit()

            quantified_ingredient = QuantifiedIngredient(quantity=float(quantity), units=unit, ingredient=ingredient)
            recipe.quantified_ingredients.append(quantified_ingredient) 
            # This operation automatically sets the foreign key (recipe_id) in the QuantifiedIngredient table to the ID of the corresponding recipe.

        # Process steps
        steps = request.form.getlist('step')
        for i, step_description in enumerate(steps, start=1):
            step = Step(sequence_number=i, description=step_description)
            recipe.steps.append(step)

        # Add the recipe to the database
        db.session.add(recipe)
        db.session.commit()

        # Handle file upload (photo)
        uploaded_file = request.files['photo']
        if uploaded_file.filename != '':
            content_type = uploaded_file.content_type
            if content_type == "image/png":
                file_extension = "png"
            elif content_type == "image/jpeg":
                file_extension = "jpg"
            elif content_type == "image/gif":
                file_extension = "gif"
            else:
                abort(400, f"Unsupported file type {content_type}")
                # might need to add some sort of redirect here

            # Create a new Photo object and store it into the database
            photo = model.Photo(
                user=flask_login.current_user,
                recipe=recipe,
                file_extension=file_extension
            )
            db.session.add(photo)
            db.session.commit()

            # Save the photo to the photos folder
            path = (
                Path(current_app.root_path)
                / "static"
                / "photos"
                / f"photo-{photo.id}.{file_extension}"
            )
            uploaded_file.save(path)

        # Load the user explicitly to avoid DetachedInstanceError
        db.session.refresh(recipe.user)

        flash('Recipe created successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template("main/new_recipe.html")

@bp.route("/vote/<int:recipe_id>/<string:vote_type>", methods=['POST'])
@flask_login.login_required
def vote(recipe_id, vote_type):
    # Check if user already voted on this recipe
    existing_vote = Rating.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()

    if existing_vote:
        if existing_vote.value == 1 and vote_type == 'down':
            existing_vote.value = -1
        elif existing_vote.value == -1 and vote_type == 'up':
            existing_vote.value = 1
    else:
        # Add new vote
        vote_value = 1 if vote_type == 'up' else -1
        new_vote = Rating(user_id=current_user.id, recipe_id=recipe_id, value=vote_value)
        db.session.add(new_vote)

    db.session.commit()
    return redirect(url_for('main.recipe', recipe_id=recipe_id))
