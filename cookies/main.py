import datetime
from os import abort
import dateutil.tz
from flask import Blueprint, render_template, render_template, request, redirect, url_for, flash
import flask_login
from flask_login import current_user
from .model import Recipe, QuantifiedIngredient, Step, Ingredient

from . import db
from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    user = model.User(id=1, email="mary@example.com", password="password", name="mary")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Another Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Yet another Food Title", person_count=1, cooking_time=1
        )
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(id=2, email="john@example.com", password="password", name="JohnDoe")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/bookmark")
@flask_login.login_required     #must be the user in order to view bookmarked recipes
def bookmark():
    user = model.User(id=3, email="john@example.com", password="password", name="JohnDoe")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/bookmark.html", posts=posts)

@bp.route("/recipe")
def recipe():
    user = model.User(id=4, email="test@example.com", password="password", name="testUser")
    posts = [
        model.Recipe(
            id=1, user=user, title="Food Title", person_count=1, cooking_time=1
        ),
    ]
    return render_template("main/recipe.html", posts=posts)

@bp.route("/new_recipe", methods=['GET', 'POST'])
@flask_login.login_required
def new_recipe():
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.form.get('recipe-title')
        description = request.form.get('recipe-description')
        cook_time = request.form.get('cook-time')
        num_people = request.form.get('num-people')

        # Create a new recipe and link it to the current user
        recipe = Recipe(title=title, description=description, cooking_time=cook_time, person_count=num_people, user=current_user)
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

        flash('Recipe created successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template("main/new_recipe.html")

#need a controller here to recieve form

# Handle file upload (photo)
        # if 'photo' in request.files:
        #     photo = request.files['photo']
        #     if photo.filename != '':
        #         # Check if the file extension is allowed
        #         file_extension = photo.filename.rsplit('.', 1)[1].lower()
        #         if file_extension not in ALLOWED_EXTENSIONS:
        #             flash(f"Unsupported file type: {file_extension}", 'error')
        #             return redirect(request.url)

        #         # Save the photo to the uploads folder
        #         filename = f"photo-{recipe.id}.{file_extension}"
        #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #         photo.save(file_path)

        #         # Create a new photo instance
        #         new_photo = Photo(file_extension=file_extension)
        #         new_photo.recipe = recipe  # Link the photo to the recipe

        #         # Add the photo to the database
        #         db.session.add(new_photo)
        #         db.session.commit()

        #         flash('Photo uploaded successfully!', 'success')