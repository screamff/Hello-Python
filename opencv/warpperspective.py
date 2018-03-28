#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np

if __name__=='__main__':
    if len(sys.argv)>1:
        image = cv2.imread(sys.argv[1], 0)
    else:
        print 'please input picture file'

    h,w = image.shape

    src = np.array([[0,0],[w-1,0],[0,h-1],[w-1,h-1]], np.float32)
    dst = np.array([[50,50],[w/3,50],[50,h-1],[w-1,h-1]], np.float32)

    p = cv2.getPerspectiveTransform(src,dst)
    r = cv2.warpPerspective(image,p,(w,h),borderValue=125)
    cv2.imshow('img', image)
    cv2.imshow('img2', r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
