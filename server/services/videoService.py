import cv2
import numpy as np
from ..algorithms.svm.detector import detectImg


def detectVideo(video_name):
    cap = cv2.VideoCapture(video_name)
    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()