#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
import math

if __name__=='__main__':
    if len(sys.argv)>1:
        image = cv2.imread(sys.argv[1], 0)
    else:
        print 'please input picture file'

    cv2.imwrite('img.jpg', image)
    h,w = image.shape

    #缩小两倍
    A1 = np.array([[0.5,0,0],[0,0.5,0]],np.float32)
    d1 = cv2.warpAffine(image, A1, (w,h), borderValue=125)

    #先缩小2倍，再平移
    A2 = np.array([[0.5, 0, w/4], [0, 0.5, h/4]], np.float32)
    d2 = cv2.warpAffine(image, A2, (w,h), borderValue=125)

    #在d2的基础上，绕图像的中心点旋转
    A3 = cv2.getRotationMatrix2D((w/2.0, h/2.0), 30 ,1)
    d3 = cv2.warpAffine(d2, A3, (w,h), borderValue=125)

    cv2.imshow('image',image)
    cv2.imshow('d1',d1)
    cv2.imshow('d2',d2)
    cv2.imshow('d3',d3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
