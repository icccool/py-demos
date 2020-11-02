from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from os.path import getsize
from sys import exit
from re import compile, IGNORECASE
import sys, time
import os
import smtplib
import socket
import logging


# 定义主机 帐号 密码 收件人 邮件主题
mail_info = {
    "from": "329262966@qq.com",
    "to": "jjmessage@163.com",
    "hostname": "smtp.qq.com",

    "password": "jeqhaysfkyxibjga",
    "mail_subject": "服务器异常",
    "mail_text": "hello, tomcat服务器出现异常了!,请及时处理",
    "mail_encoding": "utf-8"
}

# 发送邮件函数
def send_mail(error):
    # 定义邮件的头部信息
    # 连接SMTP服务器，然后发送信息
    server = SMTP_SSL(mail_info["hostname"], 465, timeout=2)
    # 登录邮箱
    server.login(mail_info["from"], mail_info["password"])
    # 消息体
    msg = MIMEText(error, "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    # 发送邮件
    server.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    server.quit()


def monitor(sname):
    """Send the machine IP port 20000 socket request,
    If capture the abnormal returns false.
    """
    s = socket.socket()
    s.settimeout(3)  # timeout
    host = ('127.0.0.1', 20000)
    try:  # Try connection to the host
        s.connect(host)
    except socket.error as e:
        logging.warning('[%s] service connection failed: %s \r\n' % (sname, e))
        return False
    return True


# 服务是否运行
def isRunning(process_name):
    try:
        process = len(os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines())
        if process >= 1:
            return True
        else:
            return False
    except:
        print("Check process ERROR!!!")
        return False


# 调用发送邮件函数发送邮件
if __name__ == '__main__':
    process_name = "PosApplication"
    isrunning = isRunning(process_name)
    print(isrunning)
    if isrunning == False:
        send_mail("老铁!" + process_name + "服务器挂了!")
