# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="rgb")
image = rawCapture.array

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)

# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
camera.close()
cv2.destroyAllWindows()
