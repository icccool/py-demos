import requests  # requess是第三方的，所以需要导入
import json
import time

url = 'http://localhost:8080/datasource/test'  # 登录接口地址
for n in range(0,100):
    response = requests.post(url)
    print(response.text)
