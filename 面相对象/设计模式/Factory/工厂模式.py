#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 13:51
# @Author   : FengYun
# @File     : 工厂模式.py
# @Software : PyCharm
from Entity.Dog import Dog
from Entity.Cat import Cat
'''
解决对象创建问题
解耦对象的创建和使用
包括工厂方法和抽象工厂
'''

def animal_factory(name):
    if name == "dog":
        return Dog()
    elif name == "cat":
        return Cat()
