#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# UDP的使用与TCP类似，但是不需要建立连接。
# 此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。

import socket

# SOCK_STREAM: tcp
# SOCK_DGRAM : udp
# 创建udp的socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
# 服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9000端口与TCP的9000端口可以各自绑定。
s.bind(('127.0.0.1', 9000))
print('Waiting Connection...')
while True:
    # recvfrom()方法返回数据和客户端的地址与端口
    data, address = s.recvfrom(1024) #recvfrom相当于accept + recv，同样会阻塞
    print('Receive from: %s:%s' % (address[0], address[1])) # address: ('127.0.0.1', 12345)
    s.sendto(b'Hello %s' % data, address)
