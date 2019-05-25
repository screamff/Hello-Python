# yummei图下载 进程有问题，未知
from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import threading

# r = requests.get("https://www.yuumeiart.com/")
#
# soup = BeautifulSoup(r.text, "html.parser")
# all_imgtags = soup.find_all('img')
# # print(all_imgtags.parent.h2)


def main(tag):
    try:
        if tag['data-image']:
            print('downloading:'+tag.parent.h2.string)
            pic = requests.get(tag['data-image'])
            with open(tag.parent.h2.string+'.jpg', 'wb') as f:
                f.write(pic.content)
        else:
            pass
    except KeyError:
        pass


if __name__ == '__main__':
    r = requests.get("https://www.yuumeiart.com/")
    soup = BeautifulSoup(r.text, "html.parser")
    all_imgtags = soup.find_all('img')
    for i in all_imgtags:
        t = threading.Thread(target=main, args=(i,))
        t.start()
    # print("---start---")
    # # 关闭进程池，关闭后po不再接受新的请求
    # po.close()
    # po.join()  # 等待po中所有的子进程结束，必须放在close之后
    # print("---end---")
