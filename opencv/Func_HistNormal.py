#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
if __name__=='__main__':
    src = cv2.imread(sys.argv[1],0)
    dst = cv2.normalize(src,None,0,1,cv2.NORM_MINMAX,cv2.CV_32F)
    print dst
    cv2.imshow('src',src)
    cv2.imshow('dst',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
