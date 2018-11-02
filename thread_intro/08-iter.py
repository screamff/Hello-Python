# coding:utf-8
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 拥有iter方法即是可迭代对象
    # 拥有iter和next方法即迭代器，可用作生成(return)可迭代对象

    def __iter__(self):
        """使其成为可迭代对象"""
        pass


classmate = Classmate()
classmate.add(11)
classmate.add(22)
classmate.add(33)

print "是否为可迭代对象:", isinstance(classmate, Iterable)
