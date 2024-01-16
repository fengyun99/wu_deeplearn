#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 22:04
# @Author   : FengYun
# @File     : Tanks.py
# @Software : PyCharm
class Tank(object):
    def __init__(self):
        pass

    # 坦克的移动方法
    def move(self):
        pass

    # 碰撞墙壁的方法
    def hitWalls(self):
        pass

    # 射击方法
    def shot(self):
        pass

    # 展示坦克
    def displayTank(self):
        pass


class MyTank(Tank):
    def __init__(self):
        pass

    # 碰撞敌方坦克的方法
    def hitEnemyTank(self):
        pass


class EnemyTank(Tank):
    def __init__(self):
        pass

    def hitMyTank(self):
        pass
