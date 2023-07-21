#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 14:03
# @Author   : FengYun
# @File     : Hero.py
# @Software : PyCharm
class Hero:
    def __init__(self, name):
        self.name = name
        self.blood = None
        self.attack = None
        self.job = None

    def __str__(self):
        info = ("Name {}".format(self.name), "blood: {}".format(self.blood),
                "attack: {}".format(self.attack), "job: {}".format(self.job))
        return '\n'.join(info)