#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/8 10:40
# @Author   : FengYun
# @File     : load.py
# @Software : PyCharm
rows = [
    {"city_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city_name": "Tokyo", "population": 13960000, "country": "Japan"},
    {"city_name": "Berlin", "population": 3645000, "country": "Germany"},
]

for row in rows:
    # print(*row)
    print("{city_name} is in {country} and has {population} people".format(**row))
