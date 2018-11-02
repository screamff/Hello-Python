#! python3
# coding:utf-8
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    # 拥有iter方法即是可迭代对象
    # 拥有iter和next方法即迭代器，可用作生成(return)可迭代对象

    def __iter__(self):
        """使其成为可迭代对象"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add(11)
classmate.add(22)
classmate.add(33)

print("是否为可迭代对象:", isinstance(classmate, Iterable))
for name in classmate:
    print(name)
