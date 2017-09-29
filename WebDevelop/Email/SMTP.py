#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

# 发件人邮箱信息
from_address = 'husidioi@163.com'
# 发件人邮箱SMTP服务器地址
smtp_server = 'smtp.163.com'


def send_msg(msg, to_address):
    password = input('Password: ')

    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_address, password)

    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()


# 最简单的纯文本邮件
# 像gmail这些有垃圾邮件检测，最简单的邮件会被拒收
def example1():
    to_address = ['husidioi@163.com']
    msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    send_msg(msg, to_address)


# 带有标题，发件人名称的邮件
def example2():
    # 收件人邮箱，可群发，所以为list
    # to_address = ['huxhu2333@gmail.com', 'husidioi@ruc.edu.cn']
    to_address = ['husidioi@163.com', '895220176@qq.com']
    msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    from email.header import Header
    from email.utils import formataddr

    # 注意formataddr传入的是pair，所以得是((str, str))
    # msg的'From'，'To'要经过formataddr，然后Subject不要用test这类都词，否则可能被拒收
    # 刚刚发现To可以不用有，但是From和Subject一定要有
    msg['From'] = formataddr((Header('胡小糊', 'utf-8').encode(), from_address))
    # 以及To这里的邮件地址与最终寄送到的邮箱无关，后者只和send_msg(msg， to_address)中的地址有关（list）
    # msg['To'] = formataddr((Header('天哪噜', 'utf-8').encode(), to_address[0]))
    msg['Subject'] = Header('给你的信', 'utf-8').encode()

    send_msg(msg, to_address)


# 发送附件
def example3():
    to_address = ['husidioi@163.com', '895220176@qq.com']
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.header import Header
    from email.utils import formataddr
    from email import encoders

    msg = MIMEMultipart()
    msg['From'] = formataddr((Header('胡小糊', 'utf-8').encode(), from_address))
    msg['Subject'] = Header('给你的信', 'utf-8').encode()

    # 加入图片作为附件
    with open('/Users/HXH/Documents/salaryif.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('attached_image', 'png', filename='image1.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='image1.png')
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-ID', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)


    # 发送html格式的邮件
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                        '<p><img src="cid:0"></p>' +    # 把附件附在html中
                        '</body></html>', 'html', 'utf-8'))

    send_msg(msg, to_address)


example3()