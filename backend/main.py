from backend.app import db,app
with app.app_context():
    db.drop_all()  # This will drop all the tables
    db.create_all()  # This will recreate the tables based on the current model
