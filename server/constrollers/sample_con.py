from flask import Flask, request, make_response, abort, session
from ..algorithms.svm import detector
from ..services.fileService import saveImage, getExt, fillImgExt
from ..services.network import allow_cross_domain
from ..models.transfer import BaseRtn, Rtn
from ..services.common import jsonify, parseJson
from ..app import app, db
from .user_con import check_auth
from ..models.pers import Image, Repo, repo_images
from ..const import IMG_DIR
from io import BytesIO
import os

"""
图片和视频的增删改查
"""
@app.route("/image", methods = ['POST'])
@allow_cross_domain
@check_auth
def uploadImg():
    img = request.files['image']
    img_name = request.form['name']
    if len(img_name) == 0:
        img_name = "未命名"
    while(1):
        try:
            img_name = fillImgExt(img_name)
            img_obj = Image(img_name)
            db.session.add(img_obj)
            db.session.commit()
            break
        except Exception as e:
            # print(str(e))
            pass
    img_full_name = os.path.join(IMG_DIR, img_obj.id + "." + getExt(img_name))
    img.save(img_full_name)
    rtn = Rtn(**parseJson(str(img_obj)))
    return jsonify(rtn)

def uploadImgs():
    pass

def modifyImg():
    pass

@app.route("/image", methods = ['DELETE'])
@allow_cross_domain
@check_auth
def deleteImg():
    data = request.get_data()
    json_obj = parseJson(data)
    image_id = json_obj['imageId']
    img = Image.query.filter_by(id=image_id).first()
    db.session.delete(img)
    img_path = os.path.join(IMG_DIR, img.id + "." + getExt(img.name))
    os.remove(img_path)
    db.session.commit()
    return jsonify(BaseRtn())

@app.route("/repo", methods = ['POST'])
@allow_cross_domain
@check_auth
def createRepo():
    data = request.get_data()
    json_obj = parseJson(data)
    max = json_obj['max']
    name = json_obj['name']
    author = session['userId']
    repo = Repo(author, name, max = int(max))
    db.session.add(repo)
    db.session.commit()
    ret = {"repo": parseJson(str(repo))}
    return jsonify(Rtn(**parseJson(str(ret))))

def addToRepo():
    pass

def modifyRepo():
    pass

def batchAddToRepo():
    pass

def removeFromRepo():
    pass

def batchRemoveFromRepo():
    pass

def analysisRepo():
    pass

def getAnalysis():
    pass

def remarkResult():
    """
    漏检、错检标记
    """
    pass

def uploadVideo():
    pass

def deleteVideo():
    pass

def modifyVideo():
    pass

def analysisVideo():
    pass


