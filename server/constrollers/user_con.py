from flask import Flask, request, make_response, abort, session
from functools import wraps
from ..algorithms.svm import detector
from ..services.fileService import saveImage
from ..services.network import allow_cross_domain
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify, parseJson
from ..app import app, db
from server.models.pers import User
import json

# 用户管理部分

def check_auth(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if not "userId" in session:
            abort(403)
        return func(*args, **kw)
    return wrapper

@app.route('/user/signIn', methods=['POST'])
@allow_cross_domain
def login():
    data = request.get_data()
    json_obj = parseJson(data)
    username = json_obj['username']
    password = json_obj['password']
    user = User(username, password)
    user_found = User.query.filter_by(username=username).first()
    if(user_found.password == user.password):
        rtn = BaseRtn()
        res = jsonify(rtn)
        session["userId"] = user_found.id
        return res, 200
    else:
        rtn = BaseRtn(code = -1, message = "login failed")
        return jsonify(rtn), 200

@app.route('/user', methods=['POST'])
@allow_cross_domain
def register():
    data = request.get_data()
    json_obj = parseJson(data)
    username = json_obj['username']
    password = json_obj['password']
    user = User(username, password)
    try:
        db.session.add(user)
        db.session.commit()
        rtn = Rtn(**parseJson(str(user)))
    except Exception as e:
        rtn = BaseRtn(code = -1, message = "register failed")
    return jsonify(rtn), 200

@app.route("/user/signIn", methods = ['DELETE'])
@allow_cross_domain
@check_auth
def signOut():
    session.pop("userId", None)
    resp = jsonify(BaseRtn())
    return resp

@app.route("/user", methods = ['GET'])
@allow_cross_domain
@check_auth
def getInfo():
    user_id = session['userId']
    user = User.query.filter_by(id=user_id).first()
    return jsonify(Rtn(**parseJson(str(user))))

@app.route("/user", methods = ['PUT'])
@allow_cross_domain
@check_auth
def changeInfo():
    data = request.get_data()
    json_obj = parseJson(data)
    username = json_obj['username']
    password = json_obj['password']
    user = User.query.filter_by(username = username).first()
    try:
        user.password = password
        db.session.commit()
    except:
        print("user info update failed")
    rtn = Rtn(**parseJson(str(user)))
    return jsonify(rtn), 200