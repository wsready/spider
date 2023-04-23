# @Time    : 2023/4/23 6:53
# @Author  : wang song
# @File    : login.py
# @Description :
# http/https协议特性：无状态。
#     - 没有请求到对应页面数据的原因：
#     - 发起的第二次基于个人主页页面请求的时候，服务器端并不知道该此请求是基于登录状态下的请求。
# cookie：用来让服务器端记录客户端的相关状态。
#     - 手动处理：通过抓包工具获取cookie值，将该值封装到headers中。（不建议）
#     - 自动处理：
#         - cookie值的来源是哪里？
#             - 模拟登录post请求后，由服务器端创建。
#         session会话对象：
#             - 作用：
#                 1.可以进行请求的发送。
#                 2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中。
#         - 创建一个session对象：session = requests.Session()
#         - 使用session对象进行模拟登录post请求的发送（cookie就会被存储在session中）
#         - session对象对个人主页对应的get请求进行发送（携带了cookie）
import requests
from lxml import etree


def spider_tcm():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    login_url = 'http://www.tcmip.cn/TCMIP/index.php/Home/Login/log_check'
    # 创建一个session对象
    session = requests.Session()
    data = {
        'uname': 'digitalcm',
        'password': 'xydnin-sazmi9-zuqPof',
        'signup1': '登陆'
    }
    # 使用session进行post请求的发送
    response = session.post(url=login_url, headers=headers, data=data)
    print(response.status_code)
    print(response.text)
    after_login_url = 'http://www.tcmip.cn/TCMIP/index.php/Home/'
    # 使用携带cookie的session进行get请求的发送
    page_text = session.get(url=after_login_url, headers=headers).text
    tree = etree.HTML(page_text)
    next_src = tree.xpath('/html/body/div[2]/div/div/div[3]/div[1]/a/@href')
    print(next_src)

if __name__ == '__main__':
    spider_tcm()
