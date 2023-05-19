#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/19 17:16
# @Author   : FengYun
# @File     : read_csv.py
# @Software : PyCharm
import pandas as pd
import numpy as np
df1 = pd.read_csv('search_data.csv')
df2 = pd.read_csv('data.csv')
print(df1['embed'][0])
test1 = np.array(df1['embed'][0])
