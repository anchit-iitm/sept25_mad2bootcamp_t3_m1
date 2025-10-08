from flask import request, jsonify, make_response
from flask_restful import Resource

from models import sample

# @app.route('/sample', methods=['GET', 'POST', 'PUT', 'DELETE'])
class sample_route(Resource):
    def get(self):
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
        
    def post(self):
        data = request.get_json()
        if not data.get('name'):
            return make_response(jsonify({"error": "Please provide a name."}), 400)
        status = sample.add(str(data.get('name')))
        if not status:
            return make_response(jsonify({"error": "Failed to add item."}), 400)
        return make_response(jsonify({"message": "Item added successfully!"}), 201)
    
    def put(self):
        data = request.get_json()
        if not data.get('id') or not data.get('new_name'):
            return make_response(jsonify({"error": "Please provide both id and new_name."}), 400)
        status = sample.edit(int(data.get('id')), str(data.get('new_name')))
        if not status:
            return make_response(jsonify({"error": "Failed to update item. Item may not exist."}), 400)
        return make_response(jsonify({"message": "Item updated successfully!"}), 200)
    
    def delete(self):
        data = request.get_json()
        if not data.get('id'):
            return make_response(jsonify({"error": "Please provide an id."}), 400)
        status = sample.delete(int(data.get('id')))
        if not status:
            return make_response(jsonify({"error": "Failed to delete item. Item may not exist."}), 400)
        return make_response(jsonify({"message": "Item deleted successfully!"}), 200)