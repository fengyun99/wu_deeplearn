#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from MyError import NoMoneyError


def demo():
    # 获取当前日期
    today = datetime.datetime.today()

    # 获取星期几
    day_of_week = today.weekday()

    # 将星期几转换为对应的字符串
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = weekdays[day_of_week]
    if day_name == "Thursday":
        raise NoMoneyError("KFC Crazy Thursday WhoEver Gives me 50 CNY, I Will Thank Him.")


if __name__ == '__main__':
    demo()
