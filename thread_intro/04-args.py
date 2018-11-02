# coding:utf-8
import threading

a = [1, 2, 3]


def test_1(list):
    print "向a列表添加4"
    list.append(4)


def test_2():
    # 多线程共享全局变量
    print "列表a：", a


# 为函数指定参数
t1 = threading.Thread(target=test_1, args=(a,))
t2 = threading.Thread(target=test_2)
t1.start()
t2.start()
