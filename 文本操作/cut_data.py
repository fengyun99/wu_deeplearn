#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/20 09:52
# @Author   : FengYun
# @File     : cut_data.py
# @Software : PyCharm
import jieba
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    sentences = [sent for sent in jieba.cut(text, cut_all=False) if sent not in ['\n', ' ']]

print(sentences)