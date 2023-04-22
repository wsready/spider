# @Time    : 2023/4/22 12:46
# @Author  : wang song
# @File    : regular_expression_01.py
# @Description : 爬取图片数据
import requests


def spider_image():
    # 1.指定url
    url = 'https://n.sinaimg.cn/sports/crawl/60/w550h310/20211230/d3e1-620a263b94e118bf3ff80d732d134125.jpg'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    # 3.请求发送
    # content返回的是一个二进制形式的图片 text返回的是字符串类型的响应数据  json返回的是对象类型的响应数据
    response = requests.get(url=url, headers=headers)
    image_data = response.content
    # 持久化存储
    with open('./nba.jpg', 'wb') as fp:
        fp.write(image_data)


if __name__ == '__main__':
    spider_image()
