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
data = {"hostName":"xxxxxx","systemInfo":"xxxx","macAddress":"address","notes":"noes","groupId":100,"netIp":"ip","timeZone":"Asia/Shanghai","cpuInfo":"cpuaaa ","hdSize":"hdsize","memSize":"memsize"}
trans_url = 'http://pos:1088/user/if_need_sync'
response2 = sess.get(trans_url, data=json.dumps(data) ,headers=header)
print(response2.text)