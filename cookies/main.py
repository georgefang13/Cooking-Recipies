import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(id=1, email="todd@email.com", password="password", name="Todd")
    recipes = [
        model.Recipe(
            1,
            title="Chocolate Chip Cookies",
            description="Classic chocolate chip cookies recipe",
            user=user,
            persons=4,
            cooking_time="30 minutes",
        ),
        model.Recipe(
            2,
            title="Spaghetti Bolognese",
            description="Homemade spaghetti bolognese with meat sauce",
            user=user,
            persons=6,
            cooking_time="45 minutes",
        ),
    ]
    return render_template("main/index.html", posts=recipes)

@bp.route("/profile")
def profile():
    user = model.User(1, email="john@example.com", name="JohnDoe")
    recipes = [
        model.Recipe(
            1,
            title="Chocolate Chip Cookies",
            description="Classic chocolate chip cookies recipe",
            user=user,
            persons=4,
            cooking_time="30 minutes",
        ),
        model.Recipe(
            2,
            title="Spaghetti Bolognese",
            description="Homemade spaghetti bolognese with meat sauce",
            user=user,
            persons=6,
            cooking_time="45 minutes",
        ),
    ]
    return render_template("main/profile.html", posts=recipes)

@bp.route("/bookmark")
def bookmark():
    user = model.User(1, email="john@example.com", name="JohnDoe")
    recipes = [
        model.Recipe(
            1,
            title="Chocolate Chip Cookies",
            description="Classic chocolate chip cookies recipe",
            user=user,
            persons=4,
            cooking_time="30 minutes",
        ),
        model.Recipe(
            2,
            title="Spaghetti Bolognese",
            description="Homemade spaghetti bolognese with meat sauce",
            user=user,
            persons=6,
            cooking_time="45 minutes",
        ),
    ]
    return render_template("main/bookmark.html", posts=recipes)

@bp.route("/recipe")
def recipe():
    user = model.User(1, email="test@example.com", name="testUser")
    recipes = [
        model.Recipe(
            1,
            title="Chocolate Chip Cookies",
            description="Classic chocolate chip cookies recipe",
            user=user,
            persons=4,
            cooking_time="30 minutes",
        )
    ]
    return render_template("main/recipe.html", post=recipes)