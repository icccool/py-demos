import requests
import json

#模拟POS请求
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

print("===========小票打印,增量全量===============================================")
headers.setdefault("access-token",json.loads(response.text)["data"]["accessToken"])
data2={
  "groupId" : 100,
  "companyId" : 10002,
  "businessId" : 100020001,
  "posId" : 12,
  "transType" : 3,
  "busiTransOrder" : 3050,
  "confLevel": 3,
  "transSqlConditions" : "",
  "transUrl" : "",
  "busiTypeName" : "小票打印",
  "busiType" : "h3_meta_print_ticket_scheme",
  "busiMainTable" : "t_print_ticket_scheme",
  "busiUnionField" : "{\"t_print_datasource\": {\"id\":\"datasource_id\"}, \"t_print_template\": {\"datasource_id\":\"datasource_id\"} }",
  "isDelete":1,
  "busiTransFrequency" : 1000,
  "dataHandleStrategy": 0,
  "busiIsSkip" : 1,
  "busiConfTryTimes": 3,
  "busiRetryTimes" : 1,
  "busiPageSize" : 50,
  "busiNotes" : "小票打印,增量全量",
  "busiConfVersion" : "1.0"
}
response2 = requests.post(url=trans_url, data=json.dumps(data2), headers=headers)
print(response2.text)


