import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "mary")
    posts = [
        model.Message(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(1, email="john@example.com", name="JohnDoe")
    posts = [
        model.Message(
            1, user=user , text="Post 1", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user=user , text="Post 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/bookmark")
def bookmark():
    user = model.User(1, email="john@example.com", name="JohnDoe")
    posts = [
        model.Message(
            1, user=user , text="Post 1", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user=user , text="Post 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/bookmark.html", posts=posts)

@bp.route("/recipe")
def recipe():
    user = model.User(1, email="test@example.com", name="testUser")
    post = [
        model.Message(
            3, user=user, text="My First Post!", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/recipe.html", post=post)