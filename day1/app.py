from flask import Flask, render_template, request, redirect, url_for

from models import db, test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///day1.sqlite3'
db.init_app(app)


@app.route("/")
def home():
    return "Hello, World!"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/page1')
def page1():
    var1 = "This is page 1, that we are making in our day1"
    bool1 = False
    return render_template('page1.html', var1_html=var1, bool1_html=bool1)

# @app.route('/page2/<int:bool1_path>')
# def page2(bool1_path):
#     var1 = "This is page 2, that we are making in our day1"
#     bool1_path = int(bool1_path)
#     if bool1_path == 1:
#         bool1 = True
#     else:
#         bool1 = False
#     # bool1 = bool1_path
#     print(bool1)
#     return render_template('page2.html', var1_html=var1, bool1_html=bool1)

@app.route('/page2/<bool1_path>/<int:int1_path>')
def page2(bool1_path, int1_path):
    var1 = "This is page 2, that we are making in our day1"
    if bool1_path.lower() == 'true':
        bool1 = True
    elif bool1_path.lower() == 'false':
        bool1 = False
    list1 = ['apple', 'banana', 'cherry']
    return render_template('page2.html', var1_html=var1, bool1_html=bool1, int1_html=int1_path, list1_html=list1)

@app.route('/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'GET':
        return render_template('page3_get.html')
    if request.method == 'POST':
        bool1_path = request.form.get('message')
        int1_path = int(request.form.get('int1_'))
        var1 = "This is page 2, that we are making in our day1"
        if bool1_path:
            bool1 = True
        else:
            bool1 = False
        list1 = ['apple', 'banana', 'cherry']
        return render_template('page3_post.html', var1_html=var1, bool1_html=bool1, int1_html=int1_path, list1_html=list1)


@app.route('/page4', methods=['GET', 'POST'])
def amar_nam_holo_method():

    if request.method == 'GET':
        all_users = test.query.all()
        message = "users found"
        if all_users == []:
            message = "No users found. Please add a user."
        return render_template('page4.html', all_users_html=all_users, message_html=message)

    if request.method == 'POST':
        if not request.form.get('name') or not request.form.get('age'):
            return "Please provide both name and age.", 400
        
        from datetime import datetime
        invalid_name = "Invalid Name " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = request.form.get('name')
        if not name:
            name = invalid_name
        age = int(request.form.get('age', 0))

        if test.query.filter_by(name=name).first():
            return "Name already exists. Please choose a different name.", 400

        new_user = test(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('amar_nam_holo_method'))

if __name__ == "__main__":
    app.run(debug=True)