# coding:utf-8
# 截取商品名称等信息，方便批量操作等
import re
import requests
from bs4 import BeautifulSoup

target_address = raw_input("输入物品连接:".decode("utf-8"))
sku_name = re.search("\d+", target_address)
sku_name = sku_name.group()
r = requests.get(target_address)
# BeautifulSoup使用编码自动检测，将当前文档设置为unicode,COOL!!
soup = BeautifulSoup(r.content, "html.parser")
# 商品名称的标签为<div class="sku-name">
# 商品价格标签为<span class="price J-p-xxxxx">x部分为商品id，即网址后面的数字

# 1.找出名字,支持css样式，但是class因为是关键词所以改加下划线
item_name = soup.find("div", class_="sku-name")

# 2.找出价格，不提供cookie貌似不会显示价格，价格标签可以检测网址数字也可使用正则匹配筛选
item_price = soup.find("span", class_=re.compile("^price J-p-\d"))

# 3.找出规格,使用搜索子节点，直接子节点为contents,children,子孙节点为descendants
choose_attr = soup.find("div", id="choose-attrs")
selected_attr = choose_attr.find("div", class_="selected")
selected_attr = selected_attr['data-value']


if __name__ == "__main__":
    print "物品名称：%s".decode("utf-8") % item_name.string.strip()
    print "物品价格：%s".decode("utf-8") % item_price
    print "物品规格：%s".decode("utf-8") % selected_attr
