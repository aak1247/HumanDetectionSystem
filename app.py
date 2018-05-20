from flask import Flask, request
from server.algorithms.svm import detector
from server.services.fileService import saveImage

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/detect', methods=['POST'])
def detect():
    img_name = "./upload.jpg"
    img = request.files['image']
    # img = saveImage(img)
    img.save(img_name)
    rects = detector.detect(img_name)
    return str(rects)

if __name__ == '__main__':
    app.run()
