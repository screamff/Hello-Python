#!/usr/bin/env python
# -*- coding:utf-8 -*-
#已失效！！！！！！
import urllib2
import re

def load_page(url):
    """
        返回html页面
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

    headers = {'user-agent':user_agent}
    req = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(req)

    return response.read()


def write_to_file(file_name, txt):
    with open(file_name, 'a') as f:
        f.write(txt)


def tieba_spider(url, begin_page, end_page):
    """
    贴吧爬虫
    """
    for i in range(begin_page, end_page+1):
        pn = (i-1) * 50
        my_url = url + str(pn)
        print "请求地址为：" + my_url

        print "正在读取第%d页" % i
        html = load_page(my_url)
        re_topic = re.compile(r'<a href\=\"/p/(.+)\" title\=\"(.+)\" target=\"_blank\" class=\"j_th_tit \"')
        topic = re_topic.findall(html)
        file_name = "steam ba.txt"
        for j in topic:
            write_to_file(file_name,"https://tieba.baidu.com/p/"+j[0])
            write_to_file(file_name, j[1])
            write_to_file(file_name, "\n")
        write_to_file(file_name, "+++++++++++++++++++++++++++++++++\n")
        print "读取第%d页===完毕" % i


if __name__ == "__main__":
    # url = raw_input("输入地址:")
    url = "https://tieba.baidu.com/f?kw=steam&ie=utf-8&pn="

    begin_page = int(raw_input("起始页码:"))
    end_page = int(raw_input("终止页码:"))
    tieba_spider(url, begin_page, end_page)
