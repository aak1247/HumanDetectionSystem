

def saveImage(img):
    return ""

def getExt(name):
    try:
        if name.find(".") != -1:
            return name.split('.')[-1]
    except:
        return "jpg"

def fillImgExt(name):
    try:
        if name.find(".") != -1:
            return name
        else:
            return name + "." + getExt(name)
    except:
        return "未命名.jpg"