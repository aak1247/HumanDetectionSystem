from flask import Flask, request, make_response, abort, session
from ..algorithms.svm import detector
from ..services.fileService import saveImage, getExt, fillImgExt
from ..services.network import allow_cross_domain
from ..services.videoService import videoDetect
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify, parseJson
from ..app import app, db
from .user_con import check_auth
from ..models.pers import Image, Repo, repo_images
from ..const import IMG_DIR
from io import BytesIO
import base64
import os
"""
包含 图片检测 视频启动检测 获取检测结果(按照资源id)
"""
@app.route("/image/detect", methods = ['POST'])
@allow_cross_domain
@check_auth
def detectImg():
    data = request.get_data()
    json_obj = parseJson(data)
    img_id = json_obj['imageId']
    img = Image.query.filter_by(id=img_id).first()
    img_path = os.path.join(IMG_DIR, img.id + "." + getExt(img.name))
    faces = detector.detect(img_path)
    img_file = open(img_path, 'rb')
    out = BytesIO()
    # img_file.readinto(out)
    rtn = {
        "faces": faces,
        "image": u"data:image/png;base64," + base64.b64encode(img_file.read()).decode('ascii')
    }
    img_file.close()
    rtn = Rtn(**rtn)
    return jsonify(rtn), 200

@app.route("/video/analysis", methods = ['POST'])
@allow_cross_domain
@check_auth
def AnalysisVideo():
    data = request.get_data()
    json_obj = jsonify(data)
    video_id = json_obj['videoId']
    # 创建job

    # 返回jobid
    return jsonify(BaseRtn()), 200

def AnalysisRepo():
    pass

def getAnalysis():
    # 获取进度和结果
    pass