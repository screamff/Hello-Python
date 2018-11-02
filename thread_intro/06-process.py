#! python3
# coding:utf-8
import multiprocessing
import time


def download_from_web(q):
    """获取数据"""
    data = [1, 2, 3, 4]
    for i in data:
        time.sleep(0.5)  # 测试当获取数据较慢时，q.empty在第一个数据时即被触发
        q.put(i)
    print("data download finish")


def analysis_data(q):
    """数据处理"""
    # 从队列读取数据
    waiting = list()
    while True:  # 此处改为try语句更合适
        data = q.get()
        waiting.append(data)
        if q.empty():
            break
    print(waiting)


def main():
    # 创建队列
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
