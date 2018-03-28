#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np
if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    out_pic = cv2.linearPolar(img, (350,350), 350, cv2.INTER_LINEAR)
    #out_pic = cv2.rotate(out_pic,1)
    cv2.imshow('I',img)
    cv2.imshow('O', out_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
