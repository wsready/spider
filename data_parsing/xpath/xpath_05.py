# @Time    : 2023/4/23 0:15
# @Author  : wang song
# @File    : xpath_05.py
# @Description : 爬取虎扑步行街主干道24h榜，并保存到excel中 https://bbs.hupu.com/topic-daily-hot
import requests
from lxml import etree
import pandas as pd


def xpath_spider_hupu():
    # 爬虫部分
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    base_url = 'https://bbs.hupu.com/topic-daily-hot-%d'
    data = []  # 用于存储数据
    for pageNum in range(1, 11):
        # 对应页码的url
        url = format(base_url % pageNum)
        response = requests.get(url=url, headers=headers)
        page_text = response.text
        tree = etree.HTML(page_text)
        div_list = tree.xpath('//*[@id="container"]/div/div[2]/div/div[2]/div[3]/ul/li/div')

        for div in div_list:
            # 局部解析
            title = div.xpath('./div[1]/a/text()')[0]
            views = div.xpath('./div[2]/text()')[0]
            author = div.xpath('./div[3]/a/text()')[0]
            time = div.xpath('./div[4]/text()')[0]
            print(title, views, author, time)
            # 将数据添加到data中
            data.append([title, views, author, time])

    # 创建DataFrame对象
    df = pd.DataFrame(data, columns=['title', 'views', 'author', 'time'])

    # 将数据写入Excel文件
    df.to_excel('hupu.xlsx', index=False)


if __name__ == '__main__':
    xpath_spider_hupu()
