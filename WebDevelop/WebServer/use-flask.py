#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

# 这里的'__name__'是指Flask在搜索的module，
# 对于single module的简单应用，使用'__name__'就OK了
# 对于大的package应用，则设置为package所在目录名
app = Flask(__name__)

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1>Welcome</h1>
                <p><button type="button" onclick="location='/login'">Log In</button></p>'''

# log in page
@app.route('/login', methods=['GET'])
def login():
    # 返回一个login的form，用于输入用户名密码来登录
    # 然后将form的内容post到对应到authenticate页
    return '''<form action="/authenticate" method="post">
                 <p><input name="username"></p>
                 <p><input name="password" type="password"></p>
                 <p><button type="submit">Log In</button></p>
                 </form>'''

# authenticate
@app.route('/authenticate', methods=['POST'])
def authenticate():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'World' and request.form['password'] == 'password':
        return '<h3>Hello, %s!</h3>' % request.form['username']
    return '<h3>Wrong username or password.</h3>'

app.run(host='127.0.0.1', port=9999)

