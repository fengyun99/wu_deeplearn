#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 20:39
# @Author   : FengYun
# @File     : 内存中读写.py
# @Software : PyCharm
# StringIO 的使用
from io import StringIO
# # 内存中读写
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('python')
# print(f.getvalue())

# 读取str
f = StringIO('hello\nnpython')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
