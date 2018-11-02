import time

d = u"--动--"
c = u"--次--"


def dong():
    for i in range(5):
        print d
        time.sleep(1)


def ci():
    for i in range(5):
        print c
        time.sleep(1)


dong()
ci()
