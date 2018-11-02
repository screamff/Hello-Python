# coding:utf-8


def create_num(all_num):
    print "---1---"
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print "---2---"
        yield a  # 函数出现yield时，此时函数成为生成器模板
        print "---3---"
        a, b = b, a+b
        current_num += 1
        print "---4---"


obj = create_num(10)

ret = next(obj)
print ret
ret = next(obj)
print ret

for num in obj:
    print num
