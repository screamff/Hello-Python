#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
img = np.zeros((512,512,3),np.uint8)
approx = np.array([[75,108],[376,77],[387,252],[83,257]])
approx2 = np.array([[20,10],[40,10],[50,100],[20,60]])
img2 = cv2.polylines(img,[approx,approx2],True,(120,255,255),5,4)
cv2.imshow('test',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
