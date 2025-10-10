from flask import render_template, request, jsonify, make_response
from . import app_api

@app_api.route('/page2/<bool1_path>/<int:int1_path>')
def page2(bool1_path, int1_path):
    var1 = "This is page 2, that we are making in our day1"
    if bool1_path.lower() == 'true':
        bool1 = True
    elif bool1_path.lower() == 'false':
        bool1 = False
    list1 = ['apple', 'banana', 'cherry']
    # return render_template('page2.html', var1_html=var1, bool1_html=bool1, int1_html=int1_path, list1_html=list1)
    return make_response(jsonify({'var1_html': var1, 'bool1_html': bool1, 'int1_html': int1_path, 'list1_html': list1}), 200)

@app_api.route('/page3', methods=['POST'])
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