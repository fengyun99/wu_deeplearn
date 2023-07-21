#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 14:04
# @Author   : FengYun
# @File     : Info.py
# @Software : PyCharm
from AddressBuilder import *
from DayBillBuilder import *


class Student:
    def __init__(self, address: Address, bill: DayBill):
        ad = AddressBuilder()
        dbb = DayBillBuilder()
        self.name = None
        self.age = None
        self.grade = None
        self.month_pocket_money = None
        self.address = ad.conf_address(address.zone, address.building, address.house_number)
        self.day_bill = dbb.conf_day_bill(bill.breakfast, bill.lunch, bill.dinner, bill.stationery, bill.game,
                                          bill.snack)
        self.lesson: list = []
        self.organize: list = []

    def __str__(self):
        return f"{self.name}年龄{self.age}现在是{self.grade},居住于{self.address}, \
        每月零花钱{self.month_pocket_money},{self.day_bill},现在的课程是{self.lesson},\
        加入的组织有{self.organize}"
