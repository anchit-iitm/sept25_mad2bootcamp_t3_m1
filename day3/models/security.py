from . import db
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) #

    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False) #
    password = db.Column(db.String(255), nullable=False) #

    login_count = db.Column(db.Integer, default=0)

    current_login_at = db.Column(db.DateTime)
    last_login_at = db.Column(db.DateTime)
    current_login_ip = db.Column(db.String(100))
    last_login_ip = db.Column(db.String(100))

    active = db.Column(db.Boolean()) #
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) #

    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<{self.id} User {self.username} - {self.email}>'

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)