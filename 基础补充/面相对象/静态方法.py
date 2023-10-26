#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 14:25
# @Author   : FengYun
# @File     : 静态方法.py
# @Software : PyCharm
# 静态方法不用参数cls
class People(object):
    country = 'china'

    @staticmethod
    # 静态方法
    def getCountry():
        return People.country


print(People.getCountry())
