import time


def work_1():
    while True:
        print "---work_1---"
        yield
        time.sleep(0.1)


def work_2():
    while True:
        print "---work_2---"
        yield
        time.sleep(0.5)


def main():
    w1 = work_1()
    w2 = work_2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()
