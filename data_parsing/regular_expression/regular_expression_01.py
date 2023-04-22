# @Time    : 2023/4/22 12:46
# @Author  : wang song
# @File    : regular_expression_01.py
# @Description : 爬取图片数据
import os
import re

import requests


def spider_re():
    if not os.path.exists('./news'):
        os.mkdir('./news')
    # 1.指定url
    url = 'https://sports.sina.com.cn/basketball/nba/2022-01-04/doc-ikyamrmz3065289.shtml'
    # 如果有多页 可以用字符串格式化写一个通用url模板
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    # 3.请求发送
    # 使用通用爬虫爬取一整张页面
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    # < divclass ="img_wrapper" >
    # < img src="//n.sinaimg.cn/sports/crawl/59/w550h309/20211230/6c5a-57f0acab58dc7a2767ea358d9a080a48.jpg" alt="" >
    # < span class ="img_descr" > < / span >
    # < / div >
    ex = '<div class="img_wrapper">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for src in img_src_list:
        # 拼接出一个完整的图片url
        src = 'https:' + src
        # 请求到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片存储的路径  new文件夹下的img_name列表
        imgPath = './news/' + img_name
        # 持久化存储
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')


if __name__ == '__main__':
    spider_re()
