# coding:utf-8
import time
import threading


def dong():
    for i in range(5):
        print "--动--".decode("utf-8")
        time.sleep(1)


def ci():
    for i in range(5):
        print "--次--".decode("utf-8")
        time.sleep(1)


t1 = threading.Thread(target=dong)
t2 = threading.Thread(target=ci)
t1.start()  # 正式启动子线程
t2.start()
print len(threading.enumerate())
# 主线程默认等待子线程结束之后才会结束
