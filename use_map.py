#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/19 09:55
# @Author   : FengYun
# @File     : 通过深度获取json对象结果.py
# @Software : PyCharm
print(list(map(lambda x: x.replace("a", "t"), "abc")))


# map(前面执行的函数名称，后面操作的数值)
def mul2(nums):
    return nums * nums


# 迭代器
for i in map(mul2, [1, 2, 3, 4, 5]):
    print(i)
