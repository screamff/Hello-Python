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
    I = cv2.imread(sys.argv[1], 0)
    Imax = np.max(I)
    Imin = np.min(I)

    Omin,Omax = 100,200
    a = float(Omax-Omin)/(Imax-Imin)
    b = Omin - a*Imin
    O = a*I + b

    O = O.astype(np.uint8)
    cv2.imshow('I',I)
    cv2.imshow('O',O)

    grayHist_I = calcGrayHist(I)
    grayHist_O = calcGrayHist(O)
    x_range = range(256)
    plt.subplot(211)
    plt.plot(x_range, grayHist_I, 'r', linewidth=2, c='black')
    plt.subplot(212)
    plt.plot(x_range, grayHist_O, 'r', linewidth=2, c='black')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
