#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/19 17:16
# @Author   : FengYun
# @File     : read_csv.py
# @Software : PyCharm
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())