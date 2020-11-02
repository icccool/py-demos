import requests  # requess是第三方的，所以需要导入
import json
import time

# ip = "127.0.0.1"
ip = "192.168.10.131"
# 模拟登陆,模拟获得网络状态
login_url = 'http://' + ip + ':1088/user/login'  # 登录接口地址
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
while 1 > 0:
    net_status_url = 'http://' + ip + ':1088/sync/sync_download_status_list'
    response2 = sess.get(net_status_url, headers=header)
    print(response2.text)
    time.sleep(2)  # 暂停2秒
