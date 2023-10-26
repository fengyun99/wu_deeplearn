#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/20 16:13
# @Author   : FengYun
# @File     : homework01.py
# @Software : PyCharm
n = 0
m = 0
while n < 9:
    if m < 5 and n < 5:
        m += 1
        print('* ' * (m-1) + '*')
    else:
        m -= 1
        print('* ' * (m-1) + '*')
    n += 1
