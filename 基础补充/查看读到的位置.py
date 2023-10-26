#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 17:20
# @Author   : FengYun
# @File     : 查看读到的位置.py
# @Software : PyCharm
# 打开一个已经存在的文件
f = open("test.txt", "r")
str = f.read(3)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
str = f.read(3)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
f.close()