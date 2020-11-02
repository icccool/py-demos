#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
db = pymysql.connect("127.0.0.1", "root", "wjb#", "h3_pos_100120587", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT * from t_promotion_base limit 1")
for i in cursor:
    print(i)
# 关闭数据库连接
db.close()