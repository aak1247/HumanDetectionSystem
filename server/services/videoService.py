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

def videoDetectTest(video_path):
    videoCapture = cv2.VideoCapture(video_path)
    while(True):
        ret, frame = videoCapture.read()
        cv2.resize(frame, (64, 128))
        rects, wei = detector.detectMultiScale(frame, winStride=(4, 4),padding=(8, 8), scale=1.05)
        if len(rects):
            for (x, y, w, h) in rects:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imwrite("./data/" + str(uuid.uuid1()) +".jpg", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    videoCapture.release()