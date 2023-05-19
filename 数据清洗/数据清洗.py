#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/11 11:29
# @Author   : FengYun
# @File     : 数据清洗.py
# @Software : PyCharm
import re

# 首先将大文本分割成小文本逐一清洗
with open("data/out.txt", "r", encoding="gbk") as f:
    lines = f.readlines()
line_list = [line for line in lines]
out_list = [''.join(line_list[0].split(' '))]
# 数据清洗第一行
# print(out_list[0])
# print(len(out_list[0]))
for i in range(1, 13):
    out_list.append(line_list[i])
# print(line_list[12])
temp_list = []
for i in range(13, 19):
    temp_list.append(line_list[i].strip())
    # text = ''.join(line_list[i])
text = '，'.join(temp_list)
pattern = re.compile(r"[。|1/1]")
content = re.sub(pattern,"",text)
out_list.append(content.strip())
temp_list.clear()
for i in range(19,64):
    out_list.append(line_list[i])
for i in range(64,67):
    temp_list.append(line_list[i].strip())
text = '，'.join(temp_list)
out_list.append(text.strip())
temp_list.clear()
for i in range(69,72):
    out_list.append(line_list[i])
text = line_list[72].strip()+line_list[73].strip()
out_list.append(text)
out_list.append(line_list[74])
text = line_list[75].strip()+line_list[76].strip()
out_list.append(text)
'''
和手动区别？差不多，简单处理后再修改？
'''