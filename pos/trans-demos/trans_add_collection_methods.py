import requests
import json

# 模拟POS请求
# url = 'http://192.168.10.131/transmission/data/get_trans_data'
url = 'http://192.168.10.131/gateway/auth/authorization/auth'
trans_url = 'http://192.168.10.131/transmission/config/add_trans_config'
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

data = {"userAccount": "1003", "userPass": "111111"}
response = requests.post(url=url, data=json.dumps(data), headers=headers)
# print(response.accessToken)
print(response.text)
print(json.loads(response.text)["data"]["accessToken"])

print("===========收款方式,增量===============================================")
headers.setdefault("access-token", json.loads(response.text)["data"]["accessToken"])
data2 = {
    "groupId": 100,
    # "companyId" : 10002,
    # "businessId" : 100020001,
    # "posId" : 12,
    "transType": 3,
    "busiTransOrder": 3050,
    "confLevel": 3,
    "transSqlConditions": "group_id = {group_id}",
    "transUrl": "",
    "busiTypeName": "收款方式信息表",
    "busiType": "h3_basic_setting_collection_methods_record",
    "busiMainTable": "t_basic_setting_collection_methods_record",
    "busiUnionField": "",
    "isDelete": 2,
    "busiTransFrequency": 1000,
    "srcHandleStrategy": 0,
    "srcHandleScript": "",
    "dstHandleStrategy": 0,
    "dstHandleScript": "",
    "busiIsSkip": 1,
    "busiConfTryTimes": 3,
    "busiRetryTimes": 1,
    "busiPageSize": 50,
    "busiNotes": "收款方式主表,增量",
    "busiConfVersion": "1.0",
    "busiMainTableId": "collection_methods_id"
}
response2 = requests.post(url=trans_url, data=json.dumps(data2), headers=headers)
print(response2.text)

# print("===========收款方式,全量增量===============================================")
# headers.setdefault("access-token", json.loads(response.text)["data"]["accessToken"])
# data2 = {
#     "groupId": 100,
#     # "companyId" : 10002,
#     # "businessId" : 100020001,
#     # "posId" : 12,
#     "transType": 3,
#     "busiTransOrder": 3050,
#     "confLevel": 3,
#     "transSqlConditions": "group_id = {group_id} and company_id={company_id} and business_id={business_id}",
#     "transUrl": "",
#     "busiTypeName": "收款方式关联表",
#     "busiType": "h3_basic_setting_collection_methods_business_relation",
#     "busiMainTable": "t_basic_setting_collection_methods_business_relation",
#     "busiUnionField": "{\"t_basic_setting_collection_methods_record\": {\"collection_methods_id\": \"collection_methods_id\"} }",
#     "isDelete": 2,
#     "busiTransFrequency": 1000,
#     "srcHandleStrategy": 0,
#     "srcHandleScript": "",
#     "dstHandleStrategy": 0,
#     "dstHandleScript": "",
#     "busiIsSkip": 1,
#     "busiConfTryTimes": 3,
#     "busiRetryTimes": 1,
#     "busiPageSize": 50,
#     "busiNotes": "收款方式主表,增量全量",
#     "busiConfVersion": "1.0",
#     "busiMainTableId": "id"
# }
# response2 = requests.post(url=trans_url, data=json.dumps(data2), headers=headers)
# print(response2.text)

print("===========机构门店信息,全量增量===============================================")
headers.setdefault("access-token", json.loads(response.text)["data"]["accessToken"])
data2 = {
    "groupId": 100,
    # "companyId" : 10002,
    # "businessId" : 100020001,
    # "posId" : 12,
    "transType": 3,
    "busiTransOrder": 3050,
    "confLevel": 3,
    "transSqlConditions": "group_id = {group_id} and org_id = {business_id}",
    "transUrl": "",
    "busiTypeName": "机构门店信息",
    "busiType": "h3_org_business_store",
    "busiMainTable": "t_org_business_store",
    "busiUnionField": "",
    "isDelete": 2,
    "busiTransFrequency": 1000,
    "srcHandleStrategy": 0,
    "srcHandleScript": "",
    "dstHandleStrategy": 0,
    "dstHandleScript": "",
    "busiIsSkip": 1,
    "busiConfTryTimes": 3,
    "busiRetryTimes": 1,
    "busiPageSize": 50,
    "busiNotes": "机构门店信息,增量全量",
    "busiConfVersion": "1.0",
    "busiMainTableId": "id"
}
response2 = requests.post(url=trans_url, data=json.dumps(data2), headers=headers)
print(response2.text)