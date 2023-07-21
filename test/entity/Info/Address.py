#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 14:45
# @Author   : FengYun
# @File     : Address.py
# @Software : PyCharm
class Address:
    def __init__(self):
        self.zone = None
        self.building = None
        self.house_number = None

    def __str__(self):
        return f"{self.zone}{self.building}{self.house_number}"
