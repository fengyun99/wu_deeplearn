#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/18 14:53
# @Author   : FengYun
# @File     : 练习3.py
# @Software : PyCharm
from sqlalchemy import *
import random
import yaml

'''
将生成的200个验证码保存到数据库中
'''


def gen_code():
    up_letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    down_letter = 'qwertyuiopasdfghjklzxcvbnm'
    number = '0123456789'
    Str = up_letter + down_letter + number
    Promo_Code = []
    Length = 7
    for _ in range(Length):
        Promo_Code.append(random.choice(Str))
    return ''.join(Promo_Code)


list_200 = []
for _ in range(200):
    list_200.append(gen_code())

# 连接数据库
with open("../config/web_sql.yaml.encode", "rb") as sql:
    sql_data = sql.read()

url = f"mysql+pymysql://{sql_data['mysql']['username']}:{sql_data['mysql']['password']}@{sql_data['ip']}:3306/dbtest" \
      f"?charset=utf8"
engine = create_engine(url, max_overflow=5)
conn = engine.connect()
for i in list_200:
    result  = conn.execute(f"insert into code set code='{i}'")
conn.connect()
