#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

connector = pymysql.connect("localhost", "root", "password", "food_nutrition", charset='utf8')
# 连接时，加入charset='utf8'，可以在输出时正确显示中文

cursor = connector.cursor()

cursor.execute("select * from food")

data = cursor.fetchall()

for row in data:
    #for column in row:
    #    print(column, end=" | ")
    print(row)