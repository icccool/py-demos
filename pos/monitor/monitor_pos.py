#!/usr/bin/python3
# -*- coding:utf8 -*-
import json
from time import sleep, time

import requests
import datetime
import time
import base64
import hashlib
from selenium import webdriver
import re
from itertools import islice
import utils.ReadConfig as ReadConfig

content_type = "application/json;charset=UTF-8"
headers = {}
headers["Content-Type"] = content_type

# 监控提示
address3 = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cedf5cd7-9ee7-4b59-8b4a-d050a3877875"

# 获得token
# 获取登录企业之后的token
def get_company_token(parameter="pro_login"):
    login_body = ReadConfig.read_config(parameter)["login"]
    test_url = ReadConfig.read_config(parameter)["address"] + "/auth/authorization/auth"
    header = {"Content-Type": "application/json; charset=UTF-8"}
    response = requests.post(test_url, data=json.dumps(login_body), headers=header)
    text = response.text
    login_access_token = json.loads(text)['data']['accessToken']

    test_url = ReadConfig.read_config(parameter)["address"] + "/auth/authorization/change_company"
    header = {"Content-Type": "application/json; charset=UTF-8"}
    header.update({"access-token": login_access_token})
    body = {"toCompanyId": ReadConfig.read_config(parameter)["company"]}
    response = requests.post(test_url, data=json.dumps(body), headers=header)
    text = response.text
    token = json.loads(text)['data']['token']
    address = ReadConfig.read_config(parameter)["address"]
    return token, address


# 发送企业微信
def send_to_wx(content):
    data1 = {
        "touser": "17521780770",
        "toparty": "",
        "totag": "",
        "msgtype": "text",
        "agentid": 1,
        "text": {
            "content": content,
            "mentioned_mobile_list": ["18616006011"]
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    requests.post(url=address3, data=json.dumps(data1), headers=headers)


if __name__ == '__main__':
    # 获得力东token
    token, address = get_company_token("pro_login")

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'access-token': token
    }

    while 1:
        # 查看监控信息 https://haidianyun.com/gateway/basedata/list/view/query/new/1002828
        test_url = ReadConfig.read_config("pro_login")["address"] + "/basedata/list/view/query/new/1002828"

        data = {"pageIndex": 1, "pageSize": 50, "sortBy": "", "sortColumn": "", "serialNumber": 0,
                "t_pos_monitor__company_id___t_org_organization_base__org_name": "",
                "t_pos_monitor__business_id___t_org_organization_base__org_name": "",
                "t_pos_monitor__online_status": [], "t_pos_monitor__pos_num": "", "t_pos_monitor__pos_version": "",
                "t_pos_monitor__update_job_exist": [], "t_pos_monitor__status": [], "t_pos_monitor__pos_time_diff": "",
                "t_pos_monitor__pos_sys_time": ["", ""], "t_pos_monitor__create_user": [],
                "t_pos_monitor__create_time": ["", ""], "t_pos_monitor__modify_user": [],
                "t_pos_monitor__modify_time": ["", ""], "listId": 719, "listViewId": 1002828,
                "_functionCode": "POSJKZXGN"}

        response = requests.post(test_url, data=json.dumps(data), headers=headers)
        # print(json.loads(response.text)["dataList"])
        for obj in json.loads(response.text)["dataList"]:
            status = (obj["t_pos_monitor__status_value"])
            if status == str(2) and obj["t_pos_monitor__online_status"] == '是':
                send_to_wx((obj["t_pos_monitor__business_id___t_org_organization_base__org_name"]) + "传输异常 !!")
        fmtTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(fmtTime + " 检测完成 !!!")
        sleep(60 * 5)
