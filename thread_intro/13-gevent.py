#! python3
# coding:utf-8
# yield-->greenlet-->gevent,封装简化
import gevent


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


print("---1---")
g1 = gevent.spawn(f1, 5)  # 与建立线程方式类似
print("---2---")
g2 = gevent.spawn(f2, 5)
print("---3---")
g3 = gevent.spawn(f3, 5)
print("---4---")
g1.join()
print("---5---")
g2.join()
print("---6---")
g3.join()
print("---7---")
