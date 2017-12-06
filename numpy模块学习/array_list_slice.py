#!/usr/bin/env python
#coding:utf-8
import numpy as np
x = np.array([[1,2,3], [4,5,6]], np.int64)
print "x.shape:",x.shape
print "x.dtype", x.dtype

y=x[0]
y[0]=9
print "y is:", y
print "x become:\n", x

print "Here is the list------"
a = [1,2,3,4,5,6]
b = a[2:5]
b[2]=9
print "b is:", b
print "a keeps:", a
