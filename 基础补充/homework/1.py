#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/24 16:27
# @Author   : FengYun
# @File     : 1.py
# @Software : PyCharm
with open('1.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        if not i.startswith('#'):
            print(i.strip('\n'))
