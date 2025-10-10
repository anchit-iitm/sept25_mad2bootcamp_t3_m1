from flask import make_response, jsonify, request
from . import app_api

@app_api.route("/")
def home():
    return "Hello, World!"

'''@app_api.route('/index')
def index():
    return render_template('index.html')'''


@app_api.route('/page1')
def page1():
    var1 = "This is page 1, that we are making in our day1"
    bool1 = False
    # return render_template('page1.html', var1_html=var1, bool1_html=bool1)
    return make_response(jsonify({'var1_html': var1, 'bool1_html': bool1}), 209)


'''# @app_api.route('/page2/<int:bool1_path>')
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

