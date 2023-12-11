# Cooking-Recipies

When starting run this:
. venv/bin/activate


Current things to do:
Update / Fix CSS with proper names for corresponding html id and class names
Get the database functioning
Look into how the database should work with ingredients / steps added as a JS function
How does the username show properly (it should show the user corresponding with the profile / recipe, not necessarily the
    user who is current_user)
Update the Jinja templates to reflect the data stored in the database, not the hardcoded text / images



from cookies import db, create_app
app=create_app()
with app.app_context():
    db.create_all()

My mistake with the data base was there are two cookies.py files. One in the root directory and one in the instance directory. To check if tables were made after running the above command, you need to do sqlite3 instance/cookies.db when using the SQLite command-line tool. 


To manually add a user:
from cookies import create_app, db
from cookies.model import User
app = create_app()
with app.app_context():
    new_user = User(email="newuser@example.com", password="password", name="New User")
    db.session.add(new_user)
    db.session.commit()

To see if the user was added:
from cookies import create_app, db
from cookies.model import User

app = create_app()

with app.app_context():
    queried_user = User.query.filter_by(email="george.fang@duke.edu").first()

if queried_user:
    print(f"User found: {queried_user}")
else:
    print("User not found.")


To see if the recipe was added:
from cookies import create_app, db
from cookies.model import Recipe

app = create_app()

with app.app_context():
    queried_recipe = Recipe.query.filter_by(title="Bread Test").first()

if queried_recipe:
    print(f"Recipe found: {queried_recipe}")
    print(f"Title: {queried_recipe.title}")
    print(f"Description: {queried_recipe.description}")
    print(f"Cooking Time: {queried_recipe.cooking_time}")
    print(f"Person Count: {queried_recipe.person_count}")
    print(f"User: {queried_recipe.user}")
    print(f"Quantified Ingredients: {queried_recipe.quantified_ingredients}")
    print(f"Steps: {queried_recipe.steps}")
else:
    print("Recipe not found.")