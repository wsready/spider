# @Time    : 2023/4/22 19:14
# @Author  : wang song
# @File    : xpath_01.py
# @Description : 最常用且最便捷高效的一种解析方式。通用性高
# xpath解析原理：
#     - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。 -from lxml import etree
#     - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
# - 如何实例化一个etree对象:from lxml import etree
#     - 1.将本地的html文档中的源码数据加载到etree对象中：
#         etree.parse(filePath)
#     - 2.可以将从互联网上获取的源码数据加载到该对象中
#         etree.HTML('page_text')
#     - xpath('xpath表达式')

# xpath表达式:
#     - /:表示的是从根节点开始定位。表示的是一个层级。
#     - //:表示的是多个层级。可以表示从任意位置开始定位。
#     - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
#     - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
#     - 取文本：
#         - /text() 获取的是标签中直系的文本内容
#         - //text() 标签中非直系的文本内容（所有的文本内容）
#     - 取属性：
#         /@attrName     ==>img/src
from lxml import etree


def xpath_spider():
    # 实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    # /:表示的是从根节点开始定位。表示的是一个层级。
    r1 = tree.xpath('/html/head/title')
    # //:表示的是多个层级。可以表示从任意位置开始定位。
    # r2 r3 等价
    r2 = tree.xpath('/html/body/div')
    r3 = tree.xpath('/html//div')
    # 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
    r4 = tree.xpath('//div[@class="song"]')
    # 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
    r5 = tree.xpath('//div[@class="song"]/p[3]')
    # 取文本：
    # /text() 获取的是标签中直系的文本内容
    r6 = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
    # //text() 标签中非直系的文本内容（所有的文本内容）
    r7 = tree.xpath('//div[@class="tang"]//text()')
    # 取属性：
    # /@属性名  /@src
    r8 = tree.xpath('//div[@class="song"]/img/@src')
    print(r8)


if __name__ == '__main__':
    xpath_spider()
