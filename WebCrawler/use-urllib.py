from urllib import request

# GET

# req = 'https://github.com/MarcoHuXHu'

req = request.Request('https://www.baidu.com')

# 把请求伪装成浏览器，例如，模拟iPhone 6去请求
#req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print(k, ":", v)
    print('Data: ', data.decode('utf-8'))
