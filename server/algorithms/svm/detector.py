import cv2
import numpy as np
from server.services.common import strs

hog = cv2.HOGDescriptor()
hog.setSVMDetector(hog.getDefaultPeopleDetector())

def detect(img_name):
    resize_scale = 0.8
    img = cv2.imread(img_name)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects, wei = hog.detectMultiScale(img, winStride=(4, 4),padding=(8, 8), scale=1.05)
    for i in range(len(rects)):
        (x, y, w, h) = rects[i]
        print("rect before:" + strs(x, "," , y, ",", w, ",", h))
        print("????")
        x0 = x + w /2
        y0 = y + h /2
        w = w * resize_scale
        x = x0 - w / 2
        x = int(x)
        w = int(w)
        h = h * resize_scale
        y = y0 - h / 2
        h = int(h)
        y = int(y)
        print("rect after:" + strs(x, "," , y, ",", w, ",", h))
        rects[i] = (x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite(img_name, img)
    return rects

def detectImg(img):
    resize_scale = 0.8
    rects, wei = hog.detectMultiScale(img, winStride=(4, 4),padding=(8, 8), scale=1.05)
    for i in range(len(rects)):
        (x, y, w, h) = rects[i]
        print("rect before:" + strs(x, "," , y, ",", w, ",", h))
        print("????")
        x0 = x + w /2
        y0 = y + h /2
        w = w * resize_scale
        x = x0 - w / 2
        x = int(x)
        w = int(w)
        h = h * resize_scale
        y = y0 - h / 2
        h = int(h)
        y = int(y)
        print("rect after:" + strs(x, "," , y, ",", w, ",", h))
        rects[i] = (x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return rects