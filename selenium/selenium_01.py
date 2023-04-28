# @Time    : 2023/4/23 9:31
# @Author  : wang song
# @File    : selenium_01.py
# @Description : selenium模块的基本使用
# 问题：selenium模块和爬虫之间具有怎样的关联？
#
# - 便捷的获取网站中动态加载的数据
#   - 便捷实现模拟登录
#     什么是selenium模块？
#     - 基于浏览器自动化的一个模块。
from time import sleep

from lxml import etree
from selenium import webdriver

# 实例化一个浏览器对象，（传入浏览器驱动）
bro = webdriver.Chrome()
# 让浏览器发起一个指定url对应请求
bro.get('https://bbs.hupu.com/topic-daily')

# page_source获取浏览器当前页面的页面源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="container"]/div/div[2]/div/div[2]/div[3]/ul/li/div/div[1]')
for li in li_list:
    name = li.xpath('./a/text()')[0]
    print(name)
sleep(5)
bro.quit()
