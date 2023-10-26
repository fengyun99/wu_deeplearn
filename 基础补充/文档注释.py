#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 21:52
# @Author   : FengYun
# @File     : 文档注释.py
# @Software : PyCharm
def print_star(n):
    """根据传入的 n，打印多个星号"""
    print("*" * n)


# 使用函数的属性"__doc__"获取文档注释
print(print_star.__doc__)
print('--------------------------------')
# 直接使用 help 函数获取函数的文档注释
help(print_star)
