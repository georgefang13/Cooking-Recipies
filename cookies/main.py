import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(email="tnam@example.com", name="Talissa")
    posts = [
        model.Message(
            user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Third post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(email="tnam@example.com", name="Talissa")
    posts = [
        model.Message(
            user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Third post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/bookmark")
def bookmark():
    user = model.User(email="tnam@example.com", name="Talissa")
    posts = [
        model.Message(
            user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Third post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/bookmark.html", posts=posts)

@bp.route("/recipe")
def recipe():
    user = model.User(email="tnam@example.com", name="Talissa")
    posts = [
        model.Message(
            user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user=user, text="Third post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/recipe.html", post=posts)