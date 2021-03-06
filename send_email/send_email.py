#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
import smtplib
from email.mime.text import MIMEText
# from email.header import Header
from email.utils import formataddr

contents = ''
with open('email.html') as file_obj:
    contents = file_obj.read()

print(contents)


class SendEmail:
    def send_email(self):
        mail_host="smtp.qq.com"           # 设置服务器
        mail_user="550502661@qq.com"     # 用户名
        mail_pass="ebevmrxtzfbybfdi"      # 口令(qq邮箱非密码)

        sender = '550502661@qq.com'
        receivers = 'luchaoet@icloud.com'   # 接收邮箱，可设置为你的QQ邮箱或者其他邮箱

        # message = MIMEText('这是邮件内容，假装这里有点东西', 'plain', 'utf-8')    # 邮件正文内容
        message = MIMEText(contents, 'html', 'utf-8')
        message["From"] = formataddr(["YUMI", '550502661@qq.com'])
        message["To"] = formataddr(["Lucy", 'luchaoet@icloud.com'])
        message['Subject'] = '邮件标题'

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.connect(mail_host, 465)        # 25 为 SMTP 端口号  qq 465 587
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
            
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
             
notice = SendEmail()
notice.send_email()