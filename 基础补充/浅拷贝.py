#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 22:06
# @Author   : FengYun
# @File     : 浅拷贝.py
# @Software : PyCharm
import copy


# 特点，浅拷贝子对象共享，导致了[[]]内容一样

def aCopy():
    '''测试浅拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print("a", a)
    print("b", b)
    b.append(30)  # ?
    b[2].append(7)
    print("浅拷贝......")
    print("a", a)
    print("b", b)


aCopy()
a = [10, 20, [5, 6]]
b = a # 同时处理
b.append(30)  # ?
b[2].append(7)
print(a)
print(b)
