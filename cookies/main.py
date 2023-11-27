import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(id=1, email="mary@example.com", name="mary")
    posts = [
        model.Message(
            id=1, user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            id=2, user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(id=1, email="john@example.com", name="JohnDoe")
    posts = [
        model.Message(
            id=1, user=user , text="Post 1", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            id=2, user=user , text="Post 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/bookmark")
def bookmark():
    user = model.User(id=1, email="john@example.com", name="JohnDoe")
    posts = [
        model.Message(
            id=1, user=user , text="Post 1", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            id=2, user=user , text="Post 2", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/bookmark.html", posts=posts)

@bp.route("/recipe")
def recipe():
    user = model.User(id=1, email="test@example.com", name="testUser")
    post = [
        model.Message(
            id=3, user=user, text="My First Post!", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/recipe.html", post=post)