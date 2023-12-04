# Cooking-Recipies

When starting run this:
. venv/bin/activate


from cookies import db, create_app
app=create_app()
with app.app_context():
    db.create_all()