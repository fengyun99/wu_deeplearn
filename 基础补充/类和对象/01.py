#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 16:05
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
class benciCar(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name + '--奔驰移动--')


class bencismartCar(benciCar):
    def move(self):
        print(self.name + '--奔驰smart移动--')


if __name__ == '__main__':
    bsc = bencismartCar('张三')
    bsc.move()
