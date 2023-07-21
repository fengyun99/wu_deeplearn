#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/6 17:31
# @Author   : FengYun
# @File     : 练习2.py
# @Software : PyCharm
'''
 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
'''
import random


def gen_code():
    up_letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    down_letter = 'qwertyuiopasdfghjklzxcvbnm'
    number = '0123456789'
    Str = up_letter + down_letter + number
    Promo_Code = []
    ALL_Promo_Code = []
    Length = 7
    for _ in range(Length):
        Promo_Code.append(random.choice(Str))
    return ''.join(Promo_Code)


list_200 = []
for _ in range(200):
    list_200.append(gen_code())

print(list_200)
