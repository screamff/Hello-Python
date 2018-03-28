#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np

if __name__=='__main__':
    if len(sys.argv)>1:
        img = cv2.imread(sys.argv[1], 0)
    else:
        print 'please input picture file'

    img = cv2.rotate(img, 0)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
