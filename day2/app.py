from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response

from models import db, test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///day1.sqlite3'
db.init_app(app)


@app.route("/")
def home():
    return "Hello, World!"

'''@app.route('/index')
def index():
    return render_template('index.html')'''


@app.route('/page1')
def page1():
    var1 = "This is page 1, that we are making in our day1"
    bool1 = False
    # return render_template('page1.html', var1_html=var1, bool1_html=bool1)
    return make_response(jsonify({'var1_html': var1, 'bool1_html': bool1}), 209)


'''# @app.route('/page2/<int:bool1_path>')
# def page2(bool1_path):
#     var1 = "This is page 2, that we are making in our day1"
#     bool1_path = int(bool1_path)
#     if bool1_path == 1:
#         bool1 = True
#     else:
#         bool1 = False
#     # bool1 = bool1_path
#     print(bool1)
#     return render_template('page2.html', var1_html=var1, bool1_html=bool1)'''

@app.route('/page2/<bool1_path>/<int:int1_path>')
def page2(bool1_path, int1_path):
    var1 = "This is page 2, that we are making in our day1"
    if bool1_path.lower() == 'true':
        bool1 = True
    elif bool1_path.lower() == 'false':
        bool1 = False
    list1 = ['apple', 'banana', 'cherry']
    # return render_template('page2.html', var1_html=var1, bool1_html=bool1, int1_html=int1_path, list1_html=list1)
    return make_response(jsonify({'var1_html': var1, 'bool1_html': bool1, 'int1_html': int1_path, 'list1_html': list1}), 200)

@app.route('/page3', methods=['POST'])
def page3():
    # if request.method == 'GET':
    #     return render_template('page3_get.html')
    if request.method == 'POST':
        data = request.get_json()
        bool1_path = data.get('bool_')
        int1_path = data.get('int1_')
        # print(type(bool1_path), type(int1_path))
        var1 = "This is page 2, that we are making in our day1"
        # if bool1_path:
        #     bool1 = True
        # else:
        #     bool1 = False
        list1 = ['apple', 'banana', 'cherry']
        # return render_template('page3_post.html', var1_html=var1, bool1_html=bool1, int1_html=int1_path, list1_html=list1)
        return make_response(jsonify({'var1_html': var1, 'bool1_html': bool1_path, 'int1_html': int1_path, 'list1_html': list1}), 200)


@app.route('/page4', methods=['GET', 'POST'])
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


@app.route('/sample', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sample_route():
    from models import sample
    if request.method == 'GET':
        if request.get_json().get('id'):
            return make_response(
                jsonify(
                    {
                        "data": sample.find_by_id(request.get_json().get('id')),
                        "message": "Item found" if sample.find_by_id(request.get_json().get('id')) else "Item not found"
                    }
                     ),
                    200)
        else: 
            data_fetched = sample.find_all()
            return make_response(
                jsonify(
                    {
                        "data": data_fetched,
                        "message": "All items fetched" if data_fetched else "No items found"
                    }
                ), 200)
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('name'):
            return make_response(jsonify({"error": "Please provide a name."}), 400)
        status = sample.add(str(data.get('name')))
        if not status:
            return make_response(jsonify({"error": "Failed to add item."}), 400)
        return make_response(jsonify({"message": "Item added successfully!"}), 201)
    if request.method == 'PUT':
        data = request.get_json()
        if not data.get('id') or not data.get('new_name'):
            return make_response(jsonify({"error": "Please provide both id and new_name."}), 400)
        status = sample.edit(int(data.get('id')), str(data.get('new_name')))
        if not status:
            return make_response(jsonify({"error": "Failed to update item. Item may not exist."}), 400)
        return make_response(jsonify({"message": "Item updated successfully!"}), 200)
    if request.method == 'DELETE':
        data = request.get_json()
        if not data.get('id'):
            return make_response(jsonify({"error": "Please provide an id."}), 400)
        status = sample.delete(int(data.get('id')))
        if not status:
            return make_response(jsonify({"error": "Failed to delete item. Item may not exist."}), 400)
        return make_response(jsonify({"message": "Item deleted successfully!"}), 200)

if __name__ == "__main__":
    app.run(debug=True)