from flask import Flask, request, jsonify
from ..algorithms.svm import detector
from ..services.fileService import saveImage
from ..services.common import allow_cross_domain
from ..app import app, db
import json




@app.route('/hello', methods=['POST', 'GET'])
@allow_cross_domain
def hello_world():
    return "hello world"

@app.route('/detect', methods=['POST'])
@allow_cross_domain
def detect():
    img_name = "./upload.jpg"
    img = request.files['image']
    # img = saveImage(img)
    img.save(img_name)
    rects = detector.detect(img_name)
    response = str(rects)
    res = jsonify(response)
    return res

@app.route('/login', methods=['POST'])
@allow_cross_domain
def login():
    from server.model import User
    data = request.get_data()
    json_obj = json.loads(data)
    username = json_obj['username']
    password = json_obj['username']
    user = User(username, password)
    return jsonify(user)

@app.route('/register', methods=['POST'])
@allow_cross_domain
def register():
    from server.model import User
    data = request.get_data()
    json_obj = json.loads(data)
    username = json_obj['username']
    password = json_obj['username']
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user)

@app.errorhandler(400)
@allow_cross_domain
def handle400():
    pass


# @app.route('/detect', method=['POST'])
# @allow_cross_domain
# def uploadImag():
#     pass

# initController(app)
