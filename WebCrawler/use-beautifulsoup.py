#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request

def crawler_dongqiudi(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as response:
        data = response.read()
        with open('index.html', 'wb') as f:
            f.write(data)

    soup = BeautifulSoup(open('index.html'))

    print(soup.head.contents)

    for child in soup.body.children:
        print(child.string)


crawler_dongqiudi('https://www.dongqiudi.com/team/50000515.html')