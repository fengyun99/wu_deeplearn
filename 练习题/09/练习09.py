#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/31 15:35
# @Author   : FengYun
# @File     : 练习09.py
# @Software : PyCharm
import re

import requests

'''
一个HTML文件，找出里面的正文/链接
通用模板：再爬取的网页中，标签低密度，中文高密度的位置就是中文的段落
'''
url = "https://zhuanlan.zhihu.com/p/26192335"
res = requests.get(url)
print(res.text)


# 统计中文字符在所有字符中的占比
def count_chn(text):
    pattern = re.compile(u'[\u1100-\uFFFDh]+?')
    result = pattern.findall(text)
    ch_num = len(result)
    possible = ch_num/len(str(text))
    return (ch_num, possible)

