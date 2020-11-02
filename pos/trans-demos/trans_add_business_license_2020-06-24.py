import requests
import json

# 模拟POS请求
# url = 'http://192.168.10.131/transmission/data/get_trans_data'
url = 'http://192.168.10.131/gateway/auth/authorization/auth'
trans_url = 'http://192.168.10.131/gateway/transmission/config/add_trans_config'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'POS_HEADER_INFO': '2',
}

data = {"userAccount": "admin", "userPass": "admin123"}
response = requests.post(url=url, data=json.dumps(data), headers=headers)
# print(response.accessToken)
print(response.text)
print(json.loads(response.text)["data"]["accessToken"])

print("===========data1{增量全量}===============================================")
headers.setdefault("access-token", json.loads(response.text)["data"]["accessToken"])
data2 = {
    "busiMainTableId": "id",
    "transType": 3,
    "busiTransOrder": 3090,
    "srcHandleStrategy": 0,
    "srcHandleScript": "",
    "dstHandleStrategy": 0,
    "dstHandleScript": "",
    "confLevel": 3,
    "transSqlConditions": "",
    "transUrl": "",
    "busiTypeName": "机构证照关联表",
    "busiType": "h3_orgmanager_business_license",
    "busiMainTable": "t_org_business_license",
    "busiUnionField": "",
    "isDelete": 2,
    "busiTransFrequency": 1000,
    "dataHandleStrategy": 0,
    "busiIsSkip": 1,
    "busiConfTryTimes": 3,
    "busiRetryTimes": 1,
    "busiPageSize": 50,
    "busiNotes": "机构证照关联表,增量全量",
    "busiConfVersion": "1.0"
}
response2 = requests.post(url=trans_url, data=json.dumps(data2), headers=headers)
print(response2.text)

