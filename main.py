import json

import requests


def spider():
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    response = requests.post(url=url, headers=headers)
    dic_obj = response.json()
    # with open('./化妆品.json', 'w', encoding='utf-8') as fp:
    #     fp.write(response)
    fp = open('./化妆品.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
if __name__ == "__main__":
    spider()