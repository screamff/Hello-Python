# coding:utf-8
# 有道翻译爬虫

from bs4 import BeautifulSoup
import requests

while 1:
    words = raw_input("英文:")
    r = requests.get(r"https://dict.youdao.com/w/"+words)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "html.parser")

    if soup.find_all(id="phrsListTab"):
        tag_translation = soup.find_all(id="phrsListTab")[0]
        print "中文释义:"
        tran_string = tag_translation.find_all(class_="trans-container")
        for i in tran_string:
            for j in i.stripped_strings:
                print j
    else:
        pass

    # if soup.find_all(id="tEETrans"):
    #     tag_eetrans = soup.find_all(id="tEETrans")[0]
    #     print "英英释义"
    #     tran_string = tag_eetrans.find_all(class_="def")
    #     for i in tran_string:
    #         for j in i.stripped_strings:
    #             print j
    #     print "同义词"
    #     syn_strign = tag_eetrans.find_all(class_="search-js")
    #     for i in syn_strign:
    #         for j in i.stripped_strings:
    #             print j
    # else:pass

    if soup.find_all(id="fanyiToggle"):
        tag_youdao = soup.find_all(id="fanyiToggle")[0]
        print "有道翻译"
        for i in tag_youdao.stripped_strings:
            print i
    else:
        pass
