from . import db

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name} was added to the database'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }
   