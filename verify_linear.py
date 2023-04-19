#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/17 22:24
# @Author   : FengYun
# @File     : verify_linear.py
# @Software : PyCharm

import pandas as pd
from prettytable import PrettyTable
import matplotlib.pyplot as plt

'''
在对数据线性回归模型建立之前需要对数据进行测试验证哪些符合线性回归的要求
'''


# 首先取出数据中的最大最小值，均值，标准偏差观察，初步判断是否存在异常字段
def test_segment(filename):
    df = pd.read_csv(filename, delimiter='\t')
    # 以表格形式展示
    table = PrettyTable()
    table.field_names = ['字段', '最小值', '最大值', '均值', '标准偏差']
    table.add_row(['销售日期', df['销售日期'].min(), df['销售日期'].max(), df['销售日期'].mean().round(2), df['销售日期'].std().round(2)])
    table.add_row(['销售价格', df['销售价格'].min(), df['销售价格'].max(), df['销售价格'].mean().round(2), df['销售价格'].std().round(2)])
    table.add_row(['卧室数', df['卧室数'].min(), df['卧室数'].max(), df['卧室数'].mean().round(2), df['卧室数'].std().round(2)])
    table.add_row(['浴室数', df['浴室数'].min(), df['浴室数'].max(), df['浴室数'].mean().round(2), df['浴室数'].std().round(2)])
    table.add_row(['房屋面积', df['房屋面积'].min(), df['房屋面积'].max(), df['房屋面积'].mean().round(2), df['房屋面积'].std().round(2)])
    table.add_row(['停车面积', df['停车面积'].min(), df['停车面积'].max(), df['停车面积'].mean().round(2), df['停车面积'].std().round(2)])
    table.add_row(['楼层数', df['楼层数'].min(), df['楼层数'].max(), df['楼层数'].mean().round(2), df['楼层数'].std().round(2)])
    table.add_row(['房屋评分', df['房屋评分'].min(), df['房屋评分'].max(), df['房屋评分'].mean().round(2), df['房屋评分'].std().round(2)])
    table.add_row(['建筑面积', df['建筑面积'].min(), df['建筑面积'].max(), df['建筑面积'].mean().round(2), df['建筑面积'].std().round(2)])
    table.add_row(['地下室面积', df['地下室面积'].min(), df['地下室面积'].max(), df['地下室面积'].mean().round(2), df['地下室面积'].std().round(2)])
    table.add_row(['建筑年份', df['建筑年份'].min(), df['建筑年份'].max(), df['建筑年份'].mean().round(2), df['建筑年份'].std().round(2)])
    table.add_row(['修复年份', df['修复年份'].min(), df['修复年份'].max(), df['修复年份'].mean().round(2), df['修复年份'].std().round(2)])
    table.add_row(['纬度', df['纬度'].min(), df['纬度'].max(), df['纬度'].mean().round(2), df['纬度'].std().round(2)])
    table.add_row(['经度', df['经度'].min(), df['经度'].max(), df['经度'].mean().round(2), df['经度'].std().round(2)])
    print(table)




if __name__ == '__main__':
    test_segment("kc-train.csv")