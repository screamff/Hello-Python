#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
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

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    grayHist = calcGrayHist(img)
    x_range = range(256)
    plt.plot(x_range, grayHist, 'r', linewidth=2, c='black')
    #设置坐标轴范围和相关标签
    y_maxValue = np.max(grayHist)
    plt.axis([0,255,0,y_maxValue])
    plt.xlabel('gray Level')
    plt.ylabel('number of pixels')
    plt.show()
