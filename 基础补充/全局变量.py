#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 16:39
# @Author   : FengYun
# @File     : 全局变量.py
# @Software : PyCharm
# 在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变
# 量指向新的数据。
# 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。 int那些
# 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。 list,dict
