# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
    # show the frame
	cv2.imshow("Frame", image)

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

camera.close()
