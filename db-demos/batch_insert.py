#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
# db = pymysql.connect("192.168.10.131", "agent", "agent123", "h3-basic-setting", charset='utf8')

config = {
    'host': '192.168.10.130',
    'port': 3306,
    'user': 'agent',
    'password': 'agent123',
    'database': 'h3-basic-setting',
    'charset': 'utf8mb4'
}

# 连接数据库
db = pymysql.connect(**config)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for n in range(0,10 * 10000):
    sql = "INSERT INTO t_basic_setting_production_cp (`production_cp_id`, `group_id`, `production_cp_code`, `production_cp_name`, `production_cp_abc`, `is_enable`, `contact`, `contact_type`, `address`, `create_user`, `create_time`, `modify_user`, `modify_time`) VALUES (null, 100, '100048', '石药集团欧意药业4', 'SYJTOYYY', 1, '姜翠花', NULL, '石家庄', 1003, '2019-08-01 10:55:00', 1003, CURRENT_TIMESTAMP(3));"
    cursor.execute(sql)
    if(n % 500 ==0):
        db.commit()
        print("commit")

# 关闭数据库连接
db.close()
print("finish")