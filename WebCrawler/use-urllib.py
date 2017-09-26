#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

# urlopen(url, data, timeout)

# 最简单的GET的例子
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


# 使用headers的例子
# 通过添加headers，把请求伪装成浏览器，例如，模拟iPhone 6去请求
def url_example2():
    # 为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性
    # header = {'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'}
    # req = request.Request('https://www.baidu.com', headers=header)
    # 与下面的方法是等价的
    req = request.Request('https://www.baidu.com')
    # 如果要使用'PUT'或者'DELETE'方法
    #request.get_method = lambda: 'PUT'
    #request.get_method = lambda: 'DELETE'
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as response:
        data = response.read()
        print('Status:', response.status, response.reason)
        for k,v in response.getheaders():
            print(k, ":", v)
        #print('Data: ', data.decode('utf-8'))

# 使用POST的例子
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

    # timeout的设置，设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响
    # 比如登录微博需要一些时间，设置timeout=1基本就超时了，这是会抛出异常
    # with urlopen
    try:
        with request.urlopen(req, data=login_data.encode('utf-8'), timeout=1) as f:
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', f.read().decode('utf-8'))
    except BaseException as e:
        print(e) # <urlopen error _ssl.c:630: The handshake operation timed out>
