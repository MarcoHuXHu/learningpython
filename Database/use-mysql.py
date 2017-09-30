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

# 执行事务
# 事务机制可以确保数据一致性
try:
   # 执行SQL语句
   cursor.execute('select * from food')
   # 向数据库提交
   connector.commit()
except:
   # 发生错误时回滚
   connector.rollback()