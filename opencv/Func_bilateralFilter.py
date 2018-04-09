#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    dst = cv2.bilateralFilter(img,11,35,40)
    # dst = cv2.GaussianBlur(img,(21,15),10)
    cv2.imshow('1',img)
    cv2.imshow('2',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
