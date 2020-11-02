import requests
import json

login_url = 'http://pos:1088/user/login'  # 登录接口地址
header = {
    "Content-Type": 'application/json',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}

# 通过session模拟登录，每次请求带着session
login_data = {"userAccount": "1003", "userPass": "111111"}
sess = requests.Session()

#触发全量同步
data = {"userBase":{"id":0,"groupId":0,"userAccount":"1003","userCode":"1003","userName":"管理员","mnemonicCode":"gly","phoneNumber":"17602185611","idcard":"440304195705251085","userStatus":0,"gender":2,"birthdayCalendar":1,"birthday":"2010-01-01 00:00:00","homeAddress":"","nation":"30"},"businessVo":{"companyId":10002,"companyCode":"10002","companyName":"西安医药连锁公司","businessId":23,"businessCode":"100020001","businessName":"2榆林市医药连锁总部仓"}}
trans_url = 'http://pos:1088/user/if_need_sync'
response2 = sess.get(trans_url, data=json.dumps(data) ,headers=header)
print(response2.text)