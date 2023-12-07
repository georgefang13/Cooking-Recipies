from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    # A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # The database will be stored into the local file cookies.db, inside the subdirectory called instance that Flask will create.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cookies.db" 


    # Initialize database
    db.init_app(app)

    #database
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cookies.db"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://gavin:kyrieKitch13@localhost/Microblog"

    # db.init_app(app)
    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main

    app.register_blueprint(main.bp)

    return app
