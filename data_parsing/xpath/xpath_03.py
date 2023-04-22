# @Time    : 2023/4/22 23:22
# @Author  : wang song
# @File    : xpath_03.py
# @Description : 解析下载图片数据 https://pic.netbian.com/4kfengjing/
import os
import requests
from lxml import etree


def xpath_spider_03():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kfengjing/'
    response = requests.get(url=url, headers=headers)
    # 手动设定响应数据的编码格式 看页面元素的head的charset是什么 就设置成什么
    response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    # 创建一个文件夹
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # # 通用处理中文乱码的解决方案
        # img_name = img_name.encode('iso-8859-1').decode('gbk')

        print(img_name, img_src)
        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'pictures/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')


if __name__ == '__main__':
    xpath_spider_03()
