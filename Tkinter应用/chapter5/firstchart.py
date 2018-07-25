#!/usr/bin/env python
#coding:utf-8
# version:python2.7.15
# windows 10
# reference: python gui cookbook

# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import show
#
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# show()

from pylab import show, arange, sin, plot, pi
t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
plot(t, s)

show()
