#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# For IP sockets, the address is a pair (host, port).
s.connect(('www.sina.com.cn', 80))

# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1024字节
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break

received_data = b''.join(buffer)
s.close()
# 分离header和html本身
header, html = received_data.split(b'\r\n\r\n', 1)
print(header)
# 将html写入文件
# with open('index.html', 'wb') as f:
#    f.write(html)
