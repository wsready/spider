# @Time    : 2023/4/22 22:51
# @Author  : wang song
# @File    : xpath_02.py
# @Description : 爬58二手房内容
import requests
from lxml import etree


def xpath_spider_02():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 爬取到页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div/a/div[2]/div[1]/div[1]')
    fp = open('58.txt', 'w', encoding='utf-8')
    for div in div_list:
        # 局部解析
        title = div.xpath('./h3/text()')[0]
        print(title)
        fp.write(title + '\n')


if __name__ == '__main__':
    xpath_spider_02()
