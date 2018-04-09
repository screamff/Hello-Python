#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    dst = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(range(len(dst)), dst, 'r', linewidth=2, c='black')
    plt.show()
