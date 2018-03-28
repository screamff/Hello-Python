#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
import math
def calcGrayHist(image):
    '''
    输入图片array，返回灰度分布array
    '''
    rows,cols = image.shape
    grayHist = np.zeros([256], np.uint64)
    for r in xrange(rows):
        for c in xrange(cols):
            grayHist[image[r][c]] += 1
    return grayHist


def equalHist(image):
    rows, cols = image.shape
    grayHist = calcGrayHist(image)
    #计算累加灰度直方图
    zeroCumuMoment = np.zeros([256],np.uint32)
    for p in xrange(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p-1] + grayHist[p]
    #原0~255像素值映射之后的像素值
    outPut_q = np.zeros([256],np.uint8)
    cofficient = 256.0/(rows*cols)
    for i in xrange(256):
        q = cofficient*float(zeroCumuMoment[i]) - 1
        if q>= 0:
            outPut_q[i] = math.floor(q)
        else:
            outPut_q[p] = 0
    #得到均衡化后的图像
    equalHistImage = np.zeros(image.shape,np.uint8)
    for r in xrange(rows):
        for c in xrange(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]]
    return equalHistImage

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    image = clahe.apply(img)
    #image = cv2.equalizeHist(img)
    #image = equalHist(img)
    cv2.imshow('img',img)
    cv2.imshow('image',image)
    cv2.waitKey()
    cv2.destroyAllWindows()
