#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

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

    # 把邮件内容解析为Message对象：
    # Message对象本身可能是一个MIMEMultipart对象，包含可能不止一层的嵌套的其他MIMEBase对象
    msg = Parser().parsestr(msg_content)
    print_email(msg)

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 测试有效，并收到了提醒
    # stat()返回邮件数量和占用空间:

    server.quit()


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(s):
    # decode_header(s): 会返回一个列表（考虑到多收件人或者CC的情况）
    # [(b'\xe7\xbb\x99\xe4\xbd\xa0\xe7\x9a\x84\xe4\xbf\xa1', 'utf-8')]
    for value, charset in decode_header(s):
        if charset:
            value = value.decode(charset)
        return value


# 将邮件嵌套的各层缩进展开：
def print_email(msg, indent=0):
    # 第0层，即From，To，Subject：
    if indent == 0:
        print('Subject: %s' % decode_str(msg.get('Subject')))
        for header in ['From', 'To']:
            value = msg.get(header)
            name, address = parseaddr(value)
            # name = decode_str(name)
            print('%s: %s <%s>' % (header, decode_str(name), address))
    # 嵌套层：
    if msg.is_multipart():
        parts = msg.get_payload()
        for part in parts:
            print('%s--------------------' % ('    ' * indent))
            print_email(part, indent+1)
    # 纯文本或附件：
    else:
        if msg.get_content_type() == 'text/plain' or msg.get_content_type() == 'text/html':
            content = msg.get_payload(decode=True)
            print('%s%s' % ('    ' * indent, content.decode('utf-8'))) # 偷懒假定都用utf-8了
        else:
            print('%sAttachment: %s' % ('    ' * indent, msg.get_content_type()))


fetch_emails()
