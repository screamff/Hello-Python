#! /usr/bin/env python
# coding:utf-8
import sys
import cv2
import numpy as np

def polar(I,center,r,theta=(0,360),r_step=1.0,theta_step=360.0/(180*8)):
    """
    将圆形图进行极坐标转换，将截取的某段圆环拉升为矩形
    """
    h,w = I.shape
    #r的取值范围
    min_r,max_r = r
    #theta取值范围
    min_theta,max_theta = theta
    #输出图像的宽高
    H = int((max_r-min_r)/r_step)+1
    W = int((max_theta-min_theta)/theta_step)+1
    out_pic = 125*np.ones((H,W),I.dtype)
    #极坐标转换
    r = np.linspace(min_r,max_r,H)
    r = np.tile(r,(W,1))
    r = np.transpose(r)
    theta = np.linspace(min_theta,max_theta,W)
    theta = np.tile(theta,(H,1))
    x,y = cv2.polarToCart(r,theta,angleInDegrees=1)
    #最近邻插值
    cx,cy = center
    for i in xrange(H):
        for j in xrange(W):
            px = int(round(x[i][j])+cx)
            py = int(round(y[i][j])+cy)
            if ((px>=0 and px<=w-1)) and (py>=0 and py <=h-1):
                out_pic[i][j] = I[px][py]
    return out_pic

if __name__=='__main__':
    img = cv2.imread(sys.argv[1], 0)
    out_pic = polar(img, (350,350), (200,350))
    #out_pic = cv2.rotate(out_pic,1)
    cv2.imshow('I',img)
    cv2.imshow('O', out_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
