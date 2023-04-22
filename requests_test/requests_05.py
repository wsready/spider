# 爬成都肯德基的商店
import json

import requests

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword = input('请输入要查询的地址:')
    param = {
         'cname':'',
        'pid':'',
        'keyword':keyword,
        'pageIndex':'1',
        'pageSize':'10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

    }
    response = requests.post(url=url, params=param, headers=headers)

    res_data = response.text
    print(res_data)
    fileName = 'kfc.json'
    fp = open(fileName, 'w', encoding='utf-8')
    data = json.dump(res_data, fp=fp, ensure_ascii=False)
    print('over!!!')