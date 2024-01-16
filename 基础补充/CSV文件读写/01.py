#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 21:52
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
import csv

with open(r"1.csv") as a:
    a_csv = csv.reader(a)  # 创建 csv 对象,它是一个包含所有数据的列表，每一行为一个元素
    headers = next(a_csv)  # 获得列表对象，包含标题行的信息
    print('headers:' + str(headers))
    for row in a_csv:  # 循环打印各行内容
        print(row)
