# -*- coding: utf-8 -*-
import cv2
import numpy, time

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(0.1)
# show a frame
#cv2.imshow("capture", frame)

while 1:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
        f = 30*(x+w/2)/3.5
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print f
cap.release()
cv2.destroyAllWindows()
