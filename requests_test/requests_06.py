# @Time    : 2023/4/21 22:35
# @Author  : wang song
# @File    : requests_06.py
# @Description :
import requests
import json


def spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    id_list = []  # 存储企业的id
    all_data_list = []  # 存储所有的企业详情数据
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 参数的封装 以键值的形式封装
    for page in range(1, 50):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'xkType': '2',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        # print(detail_json,'-------------ending-----------')
        all_data_list.append(detail_json)

    # 持久化存储all_data_list
    fp = open('./allData.json', 'w', encoding='utf-8', errors='ignore')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    fp.close()
    print('over!!!')


if __name__ == "__main__":
    spider()
