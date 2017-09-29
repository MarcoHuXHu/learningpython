#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib

# 收件箱信息
email_address = 'husidioi@163.com'
pop3_server = ['pop3.163.com', '110']

def fetch_emails():
    email_password = input('Password: ')

    # 连接到POP3服务器:
    server = poplib.POP3(*pop3_server)
    # 打开调试信息以及打印POP3服务器的欢迎文字:
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))

    # 验证邮箱和密码
    server.user(email_address)
    server.pass_(email_password)

    # stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)

    # 获取最新一封邮件, 注意索引号从1开始，且1为最早的邮件:
    index = len(mails)
    # resp为取到邮件的标号，octets为占用空间
    # lines存储了邮件的原始文本的每一行
    resp, lines, octets = server.retr(index)
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 测试有效，并收到了提醒
    # stat()返回邮件数量和占用空间:

    server.quit()


fetch_emails()
