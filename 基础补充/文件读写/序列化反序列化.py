#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 21:24
# @Author   : FengYun
# @File     : 序列化反序列化.py
# @Software : PyCharm
# import pickle
#
# a = {" name ": "Tom", "age": "40"}
# # 将字典序列化并写入文件
# with open('text.txt', 'wb') as file:
#     pickle.dump(a, file)
# # 从文件中反序列化出对象
# with open('text.txt', 'rb') as file2:
#     b = pickle.load(file2)
# print(type(b))
# print(b)

import pickle

info = [1, 2, 3, 'hello', 'python']
print('原始数据：', info)
# 将对象序列化为 string
data1 = pickle.dumps(info)
# 从 string 中读出序列化前的对象
data2 = pickle.loads(data1)
print("序列化：%r" % data1)
print("反序列化： %r" % data2)
