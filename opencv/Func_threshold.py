#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    # type = 8,otsu算法
    ret,dst = cv2.threshold(img,0,255,type=8)
    cv2.imshow('1',dst)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(range(len(hist)), hist, 'r', linewidth=2, c='black')
    plt.show()
    cv2.waitKey()
    cv2.destroyAllWindows()
