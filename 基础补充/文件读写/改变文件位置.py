#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 21:07
# @Author   : FengYun
# @File     : 改变文件位置.py
# @Software : PyCharm
import os

# 获取当前的工作目录，并输出该目录
print('当前工作目录：', os.getcwd())
# 获取 path 指定的文件夹包含的文件或文件夹名称列表
print(os.listdir(os.getcwd()))
# 改变当前工作目录
os.chdir('../')
print('改变后的工作目录：', os.getcwd())
print(os.listdir(os.getcwd()))
