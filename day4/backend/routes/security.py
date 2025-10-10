from flask_restful import Resource
from flask import request, jsonify, make_response
from argon2 import PasswordHasher #argon2-cffi
from models import user_datastore, db

ph = PasswordHasher()


class login(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        password = data.get('password')

        if not user_id or not password:

            return make_response(jsonify({"message": "all required user fields needed"}), 400)
        
        user = None

        if '@' in user_id:
            user = user_datastore.find_user(email=user_id) # User.query.filter_by(email=user_id).first()
        else:
            user = user_datastore.find_user(username=user_id)

        if not user:
            return make_response(jsonify({"message": "user not found"}), 404)

        if user.active == False:
            return make_response(jsonify({"message": "contact admin"}), 401)
    
        if ph.verify(user.password, password):
            return make_response(jsonify({
                "message": "Login successful",
                "authToken": user.get_auth_token(),
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "role": user.roles[0].name if (roles:=user.roles) else 'user'
            }), 200)
        else:
            return make_response(jsonify({"message": "invalid credentials"}), 401)
    

class register(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return make_response(jsonify({"message": "please provide the required fields"}), 400)
        
        if user_datastore.find_user(email=email):
            return make_response(jsonify({"message": "user already exists"}), 409)
        
        new_user = user_datastore.create_user(email=email, password=ph.hash(password)) # User(email=email, password=password), db.session.add(new_user)

        if data.get('username_bool') == True:
            if not data.get('username'):
                return make_response(jsonify({"message": "username is required"}), 400)
            if user_datastore.find_user(username=data.get('username')):
                db.session.rollback()
                return make_response(jsonify({"message": "username already exists"}), 409)
            username = data.get('username')
            new_user.username = username
        
        user_datastore.add_role_to_user(new_user, 'user')

        db.session.commit()
  

        return make_response(jsonify({
            "message": "Signup successful",
            }), 201)