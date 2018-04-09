#! /usr/bin/env python
# coding:utf-8
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__=='__main__':
    I = cv2.imread(sys.argv[1], 0)
    # cv::MorphShapes { cv::MORPH_RECT = 0, cv::MORPH_CROSS = 1, cv::MORPH_ELLIPSE = 2 }
    s = cv2.getStructuringElement(0,(13,13))
    r = cv2.erode(I,s)
    e = I - r
    cv2.imshow('I',I)
    cv2.imshow('erode',r)
    cv2.imshow('edge',e)
    cv2.waitKey()
    cv2.destroyAllWindows()
