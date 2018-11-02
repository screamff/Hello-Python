# coding:utf-8
import threading

a = 0
# 创建一个互斥锁，默认未上锁
mutex = threading.Lock()


def test_1(num):
    global a
    # 上锁
    # 如果之前mutex已经上锁，此处将会堵塞
    mutex.acquire()
    for i in range(num):
        a += 1
    # 解锁
    print "test_1 output:", a
    mutex.release()


def test_2(num):
    global a
    mutex.acquire()
    for i in range(num):
        a += 1
    print "test_2 output:", a
    mutex.release()


def main():
    t1 = threading.Thread(target=test_1, args=(100000,))
    t2 = threading.Thread(target=test_2, args=(100000,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
