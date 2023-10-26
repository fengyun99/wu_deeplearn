#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/23 10:38
# @Author   : FengYun
# @File     : set_list.py
# @Software : PyCharm
new_list = []
mu_list = [{'a':1,'b':1,'c':'woo'},{'a':2,'b':2,'c':'wppe'},{'a':1,'b':1,'c':'woo'}]
[new_list.append(i) for i in mu_list if i not in new_list]
print(new_list)