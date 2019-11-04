#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "tengyue1023@163.com"  # 用户名
mail_pass = "b2"  # 口令

sender = 'tengyue1023@163.com'
receivers = ['tengyue1023@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('快来开会', 'plain', 'utf-8')
message['From'] = Header("年会", 'utf-8')
message['To'] = Header("公司", 'utf-8')

subject = '公司年会'
message['Subject'] = Header(subject, 'utf-8')

#try:
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
#print("邮件发送成功")
#except smtplib.SMTPException:
#print("Error: 无法发送邮件")