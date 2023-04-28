# @Time    : 2023/4/27 11:28
# @Author  : wang song
# @File    : selenium_02.py
# @Description :
from selenium import webdriver
from time import sleep

bro = webdriver.Chrome()

bro.get('https://www.taobao.com/')

# 标签定位
search_input = bro.find_element('id', 'q')
print(type(search_input))
# 标签交互
search_input.send_keys('Iphone')

# 执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
btn = bro.find_element('css selector', '.btn-search')
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
# 回退
bro.back()
sleep(2)
# 前进
bro.forward()

sleep(5)

bro.quit()
