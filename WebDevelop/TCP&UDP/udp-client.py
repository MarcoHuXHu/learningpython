#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# SOCK_STREAM: tcp
# SOCK_DGRAM : udp
# 创建udp的socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for device in [b'Adam', b'Ben', b'Cathy', b'David', b'Eric', b'Frank']:
    # 发送数据，不需要调用connect()，直接通过sendto(data, address)给服务器发数据
    s.sendto(device, ('127.0.0.1', 9000))
    print(s.recvfrom(1024))
