from flask_restful import Api

api = Api()

from .sample import sample_route
api.add_resource(sample_route, '/sample') # http://localhost:5000/api/sample (get, post, put, delete)