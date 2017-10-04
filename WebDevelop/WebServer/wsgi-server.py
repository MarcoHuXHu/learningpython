#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 一个简单的http server
from wsgiref.simple_server import make_server
# 导入自定义的application函数:
# 注：import from自定义的.py时，需要把改目录marked as source root，这样Pycharm就不会标红
from wsgiApp import application

httpserver = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on port 8000...')
httpserver.serve_forever()
