from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
    
class sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name} was added to the database'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def find_all():
        all = sample.query.all()
        if not all:
            return False
        return [item.to_dict() for item in all]

    def find_by_id(id):
        item = sample.query.get(id)
        if item:
            return item.to_dict()
        return None

    def add(name):
        if not name or sample.query.filter_by(name=name).first():
            return False
        new_sample = sample(name=name)
        db.session.add(new_sample)
        db.session.commit()
        return True

    def edit(id, new_name):
        if not new_name or not id:
            return False
        sample_to_update = sample.query.get(id)
        if sample_to_update:
            sample_to_update.name = new_name
            db.session.commit()
            return True
        return False
    
    def delete(id):
        if not id:
            return False
        sample_to_delete = sample.query.get(id)
        if sample_to_delete:
            db.session.delete(sample_to_delete)
            db.session.commit()
            return True
        return False