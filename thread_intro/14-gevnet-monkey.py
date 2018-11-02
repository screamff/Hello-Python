#! python3
# coding:utf-8
# yield-->greenlet-->gevent,封装简化
import gevent
import time
from gevent import monkey

monkey.patch_all()  # 替换原socket, threading.Lock.acquire, time.sleep等延时阻塞操作


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


gevent.joinall([
                gevent.spawn(f1, 10),
                gevent.spawn(f2, 5),
                gevent.spawn(f3, 6)
])
