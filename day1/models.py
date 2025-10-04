from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<test {self.name}>'