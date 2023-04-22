# @Time    : 2023/4/22 23:51
# @Author  : wang song
# @File    : xpath_04.py
# @Description : 解析出所有城市名称https://www.aqistudy.cn/historydata/
from lxml import etree

import requests


def xpath_spider_04():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 网页可能会出问题 先检查一下这个网页能不能打开  verify=False
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers, verify=False).text
    tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
    # hot_city_names = []
    # # 解析到了热门城市的城市名称
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     hot_city_names.append(hot_city_name)
    # # 解析的是全部城市的名称
    # all_city_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul[1]/div[2]/li')
    # all_city_names = []
    # for li in all_city_list:
    #     all_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(all_city_name)
    # print(all_city_names, len(all_city_names))

    # //div[@class="bottom"]/ul/li/          热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a  全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names, len(all_city_names))


if __name__ == '__main__':
    xpath_spider_04()
