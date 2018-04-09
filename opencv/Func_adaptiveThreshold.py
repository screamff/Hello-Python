#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    #adaptiveMethod=0,thresholdType=0,5,C=0
    dst = cv2.adaptiveThreshold(img,255,0,0,7,5)
    cv2.imshow('w',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
