#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def nothing(*arg):
    pass

if __name__=='__main__':
    I = cv2.imread(sys.argv[1], 0)
    cv2.imshow('I',I)

    r = 1
    MAX_R = 20
    cv2.namedWindow('dilate',1)
    cv2.createTrackbar('r','dilate',r,MAX_R,nothing)
    while True:
        r = cv2.getTrackbarPos('r','dilate')
        s = cv2.getStructuringElement(2,(2*r+1,2*r+1))
        d = cv2.dilate(I,s)
        cv2.imshow('dilate',d)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
