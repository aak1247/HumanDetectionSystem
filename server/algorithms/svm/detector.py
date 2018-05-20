import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(hog.getDefaultPeopleDetector())

def detect(img_name):
    img = cv2.imread(img_name)
    rects, wei = hog.detectMultiScale(img, winStride=(4, 4),padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite(img_name, img)
    return rects


