from flask_restful import Api

api = Api(prefix='/api')

from .sample import *
api.add_resource(sample_route, '/sample') # http://localhost:5000/api/sample (get, post, put, delete) 
# api.add_resource(sample_route, '/sample/<var>', '/sample') # http://localhost:5000/api/sample (get, post, put, delete) , http://localhost:5000/api/sample/<var> (get)

from .security import login, register
api.add_resource(login, '/login')
api.add_resource(register, '/register')