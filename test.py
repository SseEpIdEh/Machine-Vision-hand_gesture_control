import cv2
import mediapipe as mp
import HandModule as hm



cap = cv2.VideoCapture(0)
detector = hm.Detector()
while True:
    _, frame = cap.read()
    frame = detector.findHands(frame)
    landmarkList = detector.Position(frame , draw = False)
    if len(landmarkList) != 0:
        print(landmarkList[4])

    cv2.imshow('Webcam' , frame)
    cv2.waitKey(1)