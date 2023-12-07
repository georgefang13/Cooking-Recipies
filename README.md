# Cooking-Recipies

When starting run this:
. venv/bin/activate


from cookies import db, create_app
app=create_app()
with app.app_context():
    db.create_all()

My mistake with the data base was there are two cookies.py files. One in the root directory and one in the instance directory. To check if tables were made after running the above command, you need to do sqlite3 instance/cookies.db when using the SQLite command-line tool. 