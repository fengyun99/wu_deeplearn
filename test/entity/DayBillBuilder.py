#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 15:07
# @Author   : FengYun
# @File     : DayBillBuilder.py
# @Software : PyCharm
from Info.DayBill import DayBill
from datetime import datetime


class DayBillBuilder:
    def __init__(self):
        self._day_bill = DayBill()

    # stationery文具
    def conf_day_bill(self, breakfast: float, lunch: float, dinner: float, stationery: float, game: float, snack: dict):
        self._day_bill.breakfast = breakfast
        self._day_bill.date = f"{datetime.year}-{datetime.month}-{datetime.day}"
        self._day_bill.lunch = lunch
        self._day_bill.dinner = dinner
        self._day_bill.stationery = stationery
        self._day_bill.snack = snack
        self._day_bill.game = game

