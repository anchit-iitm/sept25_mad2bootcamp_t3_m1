from app import create_app
from models import db, user_datastore

app = create_app()

def init_roles():
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='manager', description='Manager')
    user_datastore.find_or_create_role(name='user', description='End user')
    db.session.commit()
    return "Roles initialized"

def init_admin():

    if not user_datastore.find_user(email='admin@abc.com'):
        admin_user = user_datastore.create_user(
            email='admin@abc.com',
            password='admin',
        )
        user_datastore.add_role_to_user(admin_user, 'admin')
        db.session.commit()
        return "Admin user created"
    return "Admin user already exists"


with app.app_context():
    db.create_all()
    stat_role = init_roles()
    stat_admin = init_admin()
    print(stat_role,'&', stat_admin)
