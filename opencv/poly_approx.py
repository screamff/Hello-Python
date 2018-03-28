#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1], 0)
#阈值筛选，转为二值图
ret,thresh = cv2.threshold(img,127,255,1)
#寻找轮廓mode=3,offset=2
thresh,contours,hierarchy = cv2.findContours(thresh, 3, 2)
#生成一张对比图
# thresh2 = np.copy(thresh)
# cv2.imshow('test2',thresh2)

#筛选轮廓顶点，epsilon越小，顶点更加丰富
epsilon = 0.002*cv2.arcLength(contours[1],True)
approx = cv2.approxPolyDP(contours[1],epsilon,True)
#在原图上连接顶点，画出多边形
cv2.polylines(img,[approx],True,(122,0,0),3)
# cv2.drawContours(img,contours,1,(122,0,0),2)
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print approx
