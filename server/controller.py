from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# from .algorithms.svm import detector
# from .services.fileService import saveImage
# from .app import main as app
# from .services.common import allow_cross_domain
import json

def initController(app):
    api = Api(app)
    class CreateUser(Resource):
        def post(self):
            return {'status': 'success'}
    api.add_resource(CreateUser, '/CreateUser')

# @app.route('/hello', methods=['POST', 'GET'])
# @allow_cross_domain
# def hello_world():
#     return "hello world"

# @app.route('/detect', methods=['POST'])
# @allow_cross_domain
# def detect():
#     img_name = "./upload.jpg"
#     img = request.files['image']
#     # img = saveImage(img)
#     img.save(img_name)
#     rects = detector.detect(img_name)
#     response = str(rects)
#     res = jsonify(response)
#     return res

# @app.route('/login', methods=['POST'])
# @allow_cross_domain
# def login():
#     from server.model import User
#     data = request.get_data()
#     json_obj = json.loads(data)
#     username = json_obj['username']
#     password = json_obj['username']
#     user = User(username, password)
#     return jsonify(user)

# @app.route('/register', methods=['POST'])
# @allow_cross_domain
# def register():
#     from server.model import User
#     data = request.get_data()
#     json_obj = json.loads(data)
#     username = json_obj['username']
#     password = json_obj['username']
#     user = User(username, password)
#     db.session.add(user)
#     return jsonify(user)

# @app.errorhandler(400)
# @allow_cross_domain
# def handle400():
#     pass

