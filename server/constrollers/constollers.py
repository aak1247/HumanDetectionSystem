from flask import Flask, request, make_response
from ..algorithms.svm import detector
from ..services.fileService import saveImage
from ..services.network import allow_cross_domain
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify
from ..app import app, db
import json


@app.route('/hello', methods=['POST', 'GET'])
@allow_cross_domain
def hello_world():
    rtn = BaseRtn()
    return jsonify(rtn), 200

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
    return res, 200

@app.route('/login', methods=['POST'])
@allow_cross_domain
def login():
    from server.model import User
    data = request.get_data()
    json_obj = json.loads(data)
    username = json_obj['username']
    password = json_obj['username']
    user = User(username, password)
    user_found = User.query.filter_by(username=username).first()
    print(str(user_found))
    json_obj = jsonify({
        "username": username,
        "password": password
    })
    if(user_found.password == user.password):
        print("login success@" + str(user_found.username))
        res = make_response(json_obj)
        res.set_cookie('username', username)
        return res, 200
    else:
        print("login failed")
        return jsonify({
            "status": "400"
        })
    return jsonify(user), 200

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
    return jsonify(user), 200

@app.errorhandler(400)
@allow_cross_domain
def handle400(err):
    response = dict(status=0, message="400 Bad Request")
    return jsonify(response), 400

@app.errorhandler(404)
@allow_cross_domain
def handle404(err):
    response = dict(status=0, message="404 Not Found")
    return jsonify(response), 404

@app.errorhandler(405)
@allow_cross_domain
def handle405(err):
    response = dict(status=0, message="405 Method Not Supported")
    return jsonify(response), 405
# @app.route('/detect', method=['POST'])
# @allow_cross_domain
# def uploadImag():
#     pass

