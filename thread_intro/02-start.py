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


class DaDa(threading.Thread):
    def run(self):
        for i in range(5):
            print "--da--"
            time.sleep(1)


t1 = threading.Thread(target=dong)
t2 = threading.Thread(target=ci)
t1.start()
t2.start()
t3 = DaDa()
t3.start()
