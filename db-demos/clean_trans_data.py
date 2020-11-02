#!/usr/bin/env python3
# coding: utf-8
import pymysql
import os
path1=os.path.abspath('.')
print(path1)
#情况同步时数据
try:
    db = pymysql.connect("127.0.0.1", "root", "wjb#", "h3-pos")
    c = db.cursor()
    with open(path1 + '/clean.sql', encoding='utf-8', mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            # 判断包含空行的
            if '\n' in x:
                # 替换空行为1个空格
                x = x.replace('\n', ' ')

            # 判断多个空格时
            if '    ' in x:
                # 替换为空
                x = x.replace('    ', '')

            # sql语句添加分号结尾
            sql_item = x + ';'
            # print(sql_item)
            c.execute(sql_item)
            print("执行成功sql: %s" % sql_item)
except Exception as e:
    print(e)
    print('执行失败sql: %s' % sql_item)
finally:
    # 关闭mysql连接
    c.close()
    db.commit()
    db.close()
