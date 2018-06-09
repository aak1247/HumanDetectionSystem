from flask import Flask, request, make_response, abort, session
from ..algorithms.svm import detector
from ..services.fileService import saveImage, getExt, fillImgExt
from ..services.network import allow_cross_domain
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify, parseJson
from ..app import app, db
from .user_con import check_auth
from ..models.pers import Videos
from ..const import IMG_DIR
from io import BytesIO
import os

@app.route("/video", methods = ['POST'])
@allow_cross_domain
@check_auth
def uploadVideo():
    video = request.files['video']
    video_name = request.form['name']
    if len(video_name) == 0:
        video_name = "未命名"
    while(1):
        try:
            video_name = fillVideoExt(video_name)
            video_obj = Video(video_name)
            db.session.add(video_obj)
            db.session.commit()
            break
        except Exception as e:
            # print(str(e))
            pass
    video_full_name = os.path.join(IMG_DIR, video_obj.id + "." + getExt(video_name))
    video.save(video_full_name)
    rtn = Rtn(**parseJson(str(video_obj)))
    return jsonify(rtn)