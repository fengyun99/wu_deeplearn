#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 16:40
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
class People(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("excepection_:名字长度需要大于或者等于5")


xiaoming = People("dongGe")
print(xiaoming.getName())
