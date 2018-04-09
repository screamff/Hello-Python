#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__=='__main__':
    I = cv2.imread(sys.argv[1], 0)
    cv2.imshow('I',I)
    r, i = 1, 1
    max_r, max_i = 20, 20
    cv2.namedWindow('morphology',1)
    def nothing(*args):
        pass

    cv2.createTrackbar('r','morphology',r,max_r,nothing)
    cv2.createTrackbar('i','morphology',i,max_i,nothing)

    while True:
        r = cv2.getTrackbarPos('r','morphology')
        i = cv2.getTrackbarPos('i','morphology')

        s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
        # d = cv2.morphologyEx(I,cv2.MORPH_CLOSE,s,iterations=i)
        d_2 = cv2.morphologyEx(I,cv2.MORPH_BLACKHAT,s,iterations=i)
        # cv2.imshow('morphology',d)
        cv2.imshow('morphology',d_2)
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
