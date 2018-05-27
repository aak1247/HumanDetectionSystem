from flask import Flask, request
from server.algorithms.svm import detector
from server.services.fileService import saveImage
from server.services.common import allow_cross_domain

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/detect', methods=['POST'])
@allow_cross_domain
def detect():
    img_name = "./upload.jpg"
    img = request.files['image']
    # img = saveImage(img)
    img.save(img_name)
    rects = detector.detect(img_name)
    response = str(rects)
    return response

if __name__ == '__main__':
    app.run()
