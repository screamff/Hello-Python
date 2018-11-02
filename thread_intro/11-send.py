# coding:utf-8


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        new = yield a
        print "---new---:", new
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

ret = next(obj)  # 此行执行后，函数在等号右边的yield a处暂停
print ret
# send可以传递参数
ret = obj.send("yes")  # 此处会将字符传递给new，而next方法不会给new赋值
print ret

for num in obj:
    print num  # new的值均为none
