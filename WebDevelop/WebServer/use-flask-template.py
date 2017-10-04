#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='flask-templates')

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# log in page
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# authenticate
@app.route('/authenticate', methods=['POST'])
def authenticate():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'World' and request.form['password'] == 'password':
        return render_template('welcome.html', username= request.form['username'])
    else:
        # 这里加username是为了登录失败form还保存username
        # 另外html里面只有{{message}}和{{username}}，所以这里的参数这能设置这俩，对password无效
        return render_template('login.html',  message='Bad username or password', username= request.form['username'])


app.run(host='127.0.0.1', port=9998)