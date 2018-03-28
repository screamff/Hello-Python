# -*- coding: utf-8 -*-
import cv2
import numpy, time

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(0.1)

while 1:
    ret,frame = cap.read()
    ret2,frame2 = cap2.read()
    # show a frame
    #cv2.imshow("capture", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
        x_1 = x
        y_1 = y
        h_1 = h
    for (x,y,w,h) in faces2:
        cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,0,255),2)
        x_2 = x
        y_2 = y
        h_2 = h
    z = 1900*7/(x_1 - x_2)
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print z
cap.release()
cap2.release()
cv2.destroyAllWindows()
