# -*- coding: utf-8 -*-
import cv2
import numpy

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(1):
    # get a frame
    ret,frame = cap.read()
    # show a frame
    #cv2.imshow("capture", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('img',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("pipipi.jpeg", frame)
        break


cap.release()
cv2.destroyAllWindows()
