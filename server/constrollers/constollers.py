from flask import Flask, request, make_response, abort, session
from ..algorithms.svm import detector
from ..services.fileService import saveImage
from ..services.network import allow_cross_domain
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify, parseJson
from ..app import app, db
import json

@app.route('/*', methods=['OPTIONS'])
@allow_cross_domain
def options():
    print("potion")
    return jsonify(BaseRtn()), 200

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
    rtn = str(rects)
    res = jsonify(rtn)
    return res, 200


@app.errorhandler(400)
@allow_cross_domain
def handle400(err):
    print(str(err))
    rtn = dict(code = 0, message = "400 Bad Request")
    return jsonify(rtn), 400

@app.errorhandler(404)
@allow_cross_domain
def handle404(err):
    print(str(err))
    rtn = BaseRtn(code = 0, message = "404 Not Found")
    return jsonify(rtn), 404

@app.errorhandler(405)
@allow_cross_domain
def handle405(err):
    print(str(err))
    rtn = BaseRtn(code = 0, message = "405 Method Not Supported")
    return jsonify(rtn), 405

@app.errorhandler(500)
@allow_cross_domain
def handle500(err):
    print(str(err))
    rtn = BaseRtn(code = 0, message = "500 Internal Server Error")
    return jsonify(rtn), 500

@app.errorhandler(403)
@allow_cross_domain
def handle403(err):
    print(str(err))
    rtn = BaseRtn(code = 0, message = "403 no access")
    return jsonify(rtn), 403
# @app.route('/detect', method=['POST'])
# @allow_cross_domain
# def uploadImag():
#     pass

