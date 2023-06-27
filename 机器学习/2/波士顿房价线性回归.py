#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/5 20:21
# @Author   : FengYun
# @File     : 波士顿房价线性回归.py
# @Software : PyCharm
import pandas as pd
import numpy as np
from sklearn import datasets  # 2.1
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression

# 把数据转化为pandas的形状， 在列尾加上房价price

boston_data_x,boston_data_y = fetch_openml(name="boston", version=1, as_frame=True, return_X_y=True, parser="pandas")
# print(boston_data_x)
data = pd.DataFrame(boston_data_x)
print(data)
# print(boston_data_y)
print(data.columns)