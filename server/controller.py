from flask import Flask
from flask_restful import Resource, Api

def initController(app):
    api = Api(app)
    class CreateUser(Resource):
        def post(self):
            return {'status': 'success'}
    api.add_resource(CreateUser, '/CreateUser')
