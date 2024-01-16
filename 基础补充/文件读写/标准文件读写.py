#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 20:25
# @Author   : FengYun
# @File     : 标准文件读写.py
# @Software : PyCharm
# 读取文件的大小太大了会导致内存爆炸，所以可以反复调用read(size)方法，表示文件从指针位置开始读取size个字节
try:
    # 打开文件
    f = open('testFile.txt', 'r')
    # 读取文件内容
    str = f.read()
    print(str)
    # 关闭文件
finally:
    if f:
        f.close()
