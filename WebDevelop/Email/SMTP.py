#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib


def example1():
    # 构造一个最简单的纯文本邮件
    from email.mime.text import MIMEText
    msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

    # 发件人邮箱信息
    from_address = 'husidioi@163.com'
    password = input('Password: ')
    # 发件人邮箱SMTP服务器地址
    smtp_server = 'smtp.163.com'
    # 收件人邮箱，可群发，所以为list
    to_address = ['husidioi@163.com'] # gmail有垃圾邮件检测，最简单的邮件只能发给自己了
    #['huxhu2333@gmail.com', 'husidioi@ruc.edu.cn']

    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_address, password)



    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

example1()