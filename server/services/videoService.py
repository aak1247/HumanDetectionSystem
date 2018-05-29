import cv2
import numpy as np
from ..algorithms.svm.detector import detectImg

detector = None

def initSvmDetector():
    global detector
    detector = cv2.HOGDescriptor()
    detector.setSVMDetector(detector.getDefaultPeopleDetector())

def detectVideo(video_name):
    cap = cv2.VideoCapture(video_name)
    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

def videoDetect(video_path):
    faces = []
    counts = []
    max = 0
    interval = 0
    videoCapture = cv2.VideoCapture(video_path)
    while(True):
        ret, frame = videoCapture.read()
        cv2.resize(frame, (64, 128))
        rects, wei = detector.detectMultiScale(frame, winStride=(4, 4),padding=(8, 8), scale=1.05)
        counts.append(len(rects))
        faces.append(rects)
        if len(rects) > max:
            max = len(rects)
            # for (x, y, w, h) in rects:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    videoCapture.release()
    return {
            "faces": faces,
            "counts": counts,
            "max": max,
            "interval": interval
            }