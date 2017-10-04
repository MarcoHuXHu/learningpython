#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    pass

# log in page
@app.route('/login', methods=['GET'])
def login():
    pass

# authenticate
@app.route('/authenticate', methods=['POST'])
def authenticate():
    pass