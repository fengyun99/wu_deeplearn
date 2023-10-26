#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 16:07
# @Author   : FengYun
# @File     : 引用.py
# @Software : PyCharm
a = 1
print(id(a))  # 地址
b = a
a = 2
print(id(a))  # 地址
print(a)
print(b)

a = [1, 2]
b = a
a.append(3)
print(a)
print(b)

# 可变类型 list dict
# 不可变 int float long bool str tuple

# 字典删除元素
dict_a = {'name': 'w', 'age': 18, 'time': 12}
del dict_a['time']
print(dict_a)
# 删除字典
del dict_a
