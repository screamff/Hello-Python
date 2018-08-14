#! /usr/bin/env python
# -*- coding: utf-8 -*
# 搜索关键词查找翻译，返回中英对照表
# 注意贪婪匹配
# version: python 2.7.15
# *会优先取0
# In [109]: re.search(r'(10)(.*)(6+)', '102300678').groups()
# Out[109]: ('10', '2300', '6')
# In [110]: re.search(r'(10)(.*)(6*)', '102300678').groups()
# Out[110]: ('10', '2300678', '')
# In [111]: re.search(r'(10)(.*)(6)', '102300678').groups()
# Out[111]: ('10', '2300', '6')
# # In [112]: re.search(r'(10)(.*?)(6)', '102300678').groups()
# Out[112]: ('10', '2300', '6')
# # In [113]: re.search(r'(10)(.*?)(6*)', '102300678').groups()
# Out[113]: ('10', '', '')
import re
import sys
import requests
import json

if len(sys.argv)>1:
    with open(sys.argv[1], 'r') as f:
        raw_doc = f.read()
else:
    print 'usage:python search-items.py refiner.html'

items_in_english = re.compile(r"<td.*?>([a-zA-Z]+.*?)</td>")
all_words = items_in_english.findall(raw_doc)
no_repeated_words = set(all_words)
print len(no_repeated_words)

dict = {}
patch = re.compile(r"<title>(.*) - 无人深空中文维基 | 无人深空游戏数据 | 资料 - 灰机wiki</title>")
for i in no_repeated_words:
    if len(i)<40:
        r = requests.get(r'https://nms.huijiwiki.com/wiki/' + i)
        if r.status_code == requests.codes.ok:
            chinese_name = patch.search(r.content).group(1)
            dict[i] = chinese_name
            raw_position = re.compile(r">" + (i) + r"<")
            raw_doc = raw_position.sub('>'+chinese_name+'<', raw_doc)
            print '\"' + i + '\"' + ':' + '\"' + chinese_name + '\"' 

with open('items.json', 'w') as f:
    json.dump(dict, f)
