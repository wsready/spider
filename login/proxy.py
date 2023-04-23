# @Time    : 2023/4/23 8:34
# @Author  : wang song
# @File    : proxy.py
# @Description :
# 代理：破解封IP这种反爬机制。
# 什么是代理：
# - 代理服务器。
#   代理的作用：
#   - 突破自身IP访问的限制。
#     - 隐藏自身真实IP
#       代理相关的网站：
#       - 快代理
#       - 西祠代理
#       - www.goubanjia.com
#         代理ip的类型：
#       - http：应用到http协议对应的url中
#       - https：应用到https协议对应的url中
#
# 代理ip的匿名度：
#
# - 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
#   - 匿名：知道使用了代理，不知道真实ip
#     - 高匿：不知道使用了代理，更不知道真实的ip
