# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while(1):
    # get a frame
    ret,frame = cap.read()
    ret2,frame2 = cap2.read()
    # show a frame
    cv2.imshow("capture", frame)
    cv2.imshow("capture2", frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
