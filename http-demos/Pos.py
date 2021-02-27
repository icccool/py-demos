import requests
import json

# ==========================================================
# 发送http请求
# ==========================================================


#模拟POS请求
url = 'http://192.168.10.131/transmission/data/get_trans_data'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'POS_HEADER_INFO': '2',
    'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55SWQiOjEwMDAyLCJhdXRoRm9ybSI6MSwiZ3JvdXBJZCI6MTAwLCJleHAiOjE1ODI5ODUyMTksInVzZXJJZCI6MTAwMywiaWF0IjoxNTgyMTIxMjE5fQ.P51LCsdDYUF1JcjWUzaAYdS_1_w11Hlk2yxpFitd1IU'
}

# 空的对象，body参数
data = {
    "groupId": 100,
    "companyId": 10002,
    "businessId": 23,
    "posId": "1",
    "sequenceId": 0,
    "busiType": "h3_orgmanager_user_base"
}
data = json.dumps(data)

response = requests.post(url=url, data=data, headers=headers)
print(response.url)
print(response.text)
