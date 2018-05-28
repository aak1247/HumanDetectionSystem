from flask import Flask, request, jsonify
from server.algorithms.svm import detector
from server.services.fileService import saveImage
from server.services.common import allow_cross_domain
from server.controller import initController
from datetime import timedelta

app = Flask(__name__, static_url_path='', static_folder='static/build')
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

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

@app.errorhandler(400)
@allow_cross_domain
def handle400():
    pass


# @app.route('/detect', method=['POST'])
# @allow_cross_domain
# def uploadImag():
#     pass

initController(app)

if __name__ == '__main__':
    app.run(debug=True)
