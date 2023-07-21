#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 14:50
# @Author   : FengYun
# @File     : DayBill.py
# @Software : PyCharm
class DayBill:
    def __init__(self):
        self.date = None
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        self.stationery = None
        self.game = None
        self.snack: dict = {}

    def sum_spend(self):
        snack_list = self.snack.values()
        all_spend = self.breakfast + self.lunch + self.dinner + self.stationery + self.game + sum(snack_list)
        return all_spend

    def __str__(self):
        return f"{self.date}消费了{self.sum_spend()}"