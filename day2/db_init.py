from day2.app_v1 import app
from day2.models.sample import db


with app.app_context():
    db.create_all()