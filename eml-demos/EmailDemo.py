# 首先导入email模块构造邮件
from email.mime.text import MIMEText

# 构造邮件，内容为hello world
from past.builtins import raw_input

msg = MIMEText('hello world')
# 设置邮件主题
msg["Subject"] = "hello world2"
# 寄件者
msg["From"] = ''
# 收件者
msg["To"] = ''

# 然后是导入smtplib模块发送邮件
import smtplib

#from_addr = raw_input("请输入发送方邮箱账号:")
from_addr = '329262966@qq.com'
# password = raw_input("请输入发送方邮箱密码（这里输入的内容是开启pop3/smtp服务时腾讯给出的授权码）:")
password = 'jeqhaysfkyxibjga';
# smtp服务器地址
smtp_server = 'smtp.qq.com'
# 收件人地址
# to_addr = raw_input("请输入收件人地址:")
to_addr ='jjmessage@163.com'
# smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,第一个参数是smtp服务器地址，第二个参数是端口，第三个参数是超时设置,这里必须使用ssl证书，要不链接不上服务器
server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
# 登录邮箱
server.login(from_addr, password)
# 发送邮件，第一个参数是发送方地址，第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱，msg.as_string()将MIMEText对象转化成文本
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
