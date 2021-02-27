import requests  # requess是第三方的，所以需要导入
import json
import time

# ==========================================================
# 获得session, 然后携带session请求网络
# ==========================================================


login_url = 'http://192.168.10.131:1088/user/login'  # 登录接口地址
header = {
    "Content-Type": 'application/json',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}

# Python字典数据转为json，需要使用json.dumps
login_data = {"userAccount": "1003", "userPass": "111111"}

# 通过session模拟登录，每次请求带着session
sess = requests.Session()
response1 = sess.post(login_url, data=json.dumps(login_data), headers=header)

#
while 1:
    net_status_url = 'http://192.168.10.131:1088/sync/net_status'  # 登录接口地址
    response2 = sess.get(net_status_url,  headers=header)
    print(response2.text)
    time.sleep(2) # 暂停2秒






