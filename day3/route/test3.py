from flask import render_template, request, jsonify, make_response
from flask_security import auth_required, roles_accepted, roles_required  # or, and

from . import app_api
from models import db, test

@app_api.route('/page4', methods=['GET', 'POST'])
@auth_required('token')
@roles_accepted('admin', 'user')
def amar_nam_holo_method():

    if request.method == 'GET':
        all_users = test.query.all()
        message = "users found"
        if not all_users:
            message = "No users found. Please add a user."
        list_of_users = []
        for user in all_users:
            list_of_users.append(user.to_dict())
        # return render_template('page4.html', all_users_html=all_users, message_html=message)
        return make_response(jsonify({'all_users_html': list_of_users, 'message_html': message}), 200)

    if request.method == 'POST':
        data = request.get_json()
        if not data.get('name') or not data.get('age'):
            return make_response(jsonify({"error": "Please provide both name and age."}), 400)
        
        from datetime import datetime
        invalid_name = "Invalid Name " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = data.get('name')
        if not name:
            name = invalid_name
        age = int(data.get('age', 0))

        if test.query.filter_by(name=name).first():
            return make_response(jsonify({"error": "Name already exists. Please choose a different name."}), 400)

        new_user = test(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify({"message": f"User {new_user} successfully!"}), 201)