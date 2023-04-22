# @Time    : 2023/4/22 18:08
# @Author  : wang song
# @File    : bs4_01.py
# @Description :
# 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
# 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
from bs4 import BeautifulSoup
import lxml

if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)

    # soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.a)

    # find('tagName'):等同于soup.div
    # print(soup.div)

    # 等同于print(soup.div)
    # print(soup.find('div'))

    # 属性定位：soup.find('div',class_/id/attr='song')
    # print(soup.find('div', class_='song'))

    # soup.find_all('tagName'): 返回符合要求的所有标签（列表）
    # print(soup.find_all('a'))

    # select('某种选择器（id，class，标签...选择器）'), 返回的是一个列表。
    # print(soup.select('.tang'))

    # 层级选择器：
    # - soup.select('.tang > ul > li > a')：>表示的是一个层级
    # - oup.select('.tang > ul a')：空格表示的多个层级
    # 获取标签中属性值：['属性名']
    # print(soup.select('.tang > ul a')[0]['href'])

    # 获取标签之间的文本数据：
    # - soup.a.text/string/get_text()   注意：是soup.*.xxx 如果是select会报错
    # print(soup.select('.tang > ul a')[0].text)
    # print(soup.select('.tang > ul a')[0].string)
    # print(soup.select('.tang > ul a')[0].get_text())

    # - text/get_text():可以获取某一个标签中所有的文本内容
    # - string：只可以获取该标签下面直系的文本内容
    # print(soup.find('div', class_='song').text)
    # print(soup.find('div', class_='song').get_text())
    # print(soup.find('div', class_='song').string)
