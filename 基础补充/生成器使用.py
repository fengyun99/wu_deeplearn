#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 21:40
# @Author   : FengYun
# @File     : 生成器使用.py
# @Software : PyCharm
# 生成器的使用
s = (x * 2 for x in range(5))
print(s)  # 生成器对象，只是对象
print(tuple(s))  # tuple 函数转换为元组
print(tuple(s))  # 只能访问一次元素。第二次就为空了。需要再生成一次
s = (x * 2 for x in range(5))
print('next 方法获取元素：', s.__next__())
print('next 方法获取元素：', s.__next__())
print('next 方法获取元素：', s.__next__())
print(tuple(s))  # 抛出了?
