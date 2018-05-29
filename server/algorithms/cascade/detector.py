import cv2
import numpy as np

cascade = cv2.CascadeClassifier("./haarcascade_fullbody.xml")

def detect(img_name):
    resize_scale = 1
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rects = cascade.detectMultiScale(gray, 1.1,5,cv2.CASCADE_SCALE_IMAGE,(50,50),(100,100))
    for i in range(len(rects)):
        (x, y, w, h) = rects[i]
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
        rects[i] = (x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite(img_name, img)