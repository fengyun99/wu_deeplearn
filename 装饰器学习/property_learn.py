#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/26 16:02
# @Author   : FengYun
# @File     : property_learn.py
# @Software : PyCharm

class DataSet(object):
    def __init__(self):
        self._num = 10

    # 类比getter，函数变属性
    @property
    def num(self):
        return self._num

    # 类比setter，函数变属性
    @num.setter
    def num(self, value):
        self._num = value

    # 删除
    @num.deleter
    def num(self):
        del self._num


dataset = DataSet()
# 当用_num当做参数时，可以认为是私有变量，外部不能访问，要访问只能使用get,set
print(dataset.num)
dataset.num = 20
print(dataset.num)
try:
    del dataset.num
    print(dataset.num) # 抛出异常
except AttributeError as e:
    raise e
