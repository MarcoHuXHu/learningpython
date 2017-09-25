#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

# urlopen(url, data, timeout)

# GET

# 利用urlopen(url) 直接打开url
def url_example1():
    with request.urlopen('https://github.com/MarcoHuXHu') as f:
    # urlopen参数可以传入一个request请求,它其实就是一个Request类的实例，构造时需要传入Url,Data等等的内容
    # 一般推举Request这种方法，且在例2中有用到
    #req = request.Request('https://github.com/MarcoHuXHu')
    #with request.urlopen(req) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k,v in f.getheaders():
            print(k, ":", v)
        # print('Data: ', data.decode('utf-8'))


# 把请求伪装成浏览器，例如，模拟iPhone 6去请求
def url_example2():
    req = request.Request('https://www.baidu.com')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as response:
        data = response.read()
        print('Status:', response.status, response.reason)
        for k,v in response.getheaders():
            print(k, ":", v)
        #print('Data: ', data.decode('utf-8'))

# 对于POST
# 利用parse.urlencode来封装需要POST的数据
# 然后再利用# 利用urlopen(Request, data)来发送请求
# 也可以把(url, data)装入Request中，然后urlopen(Request)
# 对于GET，直接操作url即可
# 传入参数登录微博
def url_example3():
    print('Login to weibo.cn...')
    login_data = parse.urlencode([
        ('username', 'huxhu2333@gmail.com'),
        ('password', 'husidioi'),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

url_example1()