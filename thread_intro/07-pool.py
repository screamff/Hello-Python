# coding:utf-8
from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print "%s start,pid is:" % (msg, os.getpid())
    time.sleep(random.random()*2)
    t_stop = time.time()
    print "spending time:%s" % (t_stop-t_start)


# 创建进程池，最大进程数为3
po = Pool(3)
for i in range(10):
    # 传递任务与参数
    po.apply_async(worker, (i,))
print "---start---"
# 关闭进程池，关闭后po不再接受新的请求
po.close()
po.join()  # 等待po中所有的子进程结束，必须放在close之后
print "---end---"
