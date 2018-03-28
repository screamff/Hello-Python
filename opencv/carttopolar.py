#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
x = np.array([0,1,2,0,1,2,0,1,2],np.float64)-1
y = np.array([0,0,0,1,1,1,2,2,2],np.float64)-1
r,theta = cv2.cartToPolar(x,y,1)
print r,theta
