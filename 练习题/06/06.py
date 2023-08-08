#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/31 14:01
# @Author   : FengYun
# @File     : 06.py
# @Software : PyCharm
import os
from collections import Counter
import re
'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''


def count_most_common_words(directory, file_format):
    word_counts = []
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(file_format):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # 读取日记内容
                diary_content = file.read()
                # 使用正则表达式分割单词
                words = re.findall(r'\w+', diary_content.lower())
                # 统计单词出现的次数
                word_count = Counter(words)
                word_counts.append(word_count)
    # 返回每个日记文件中出现频率最高的单词
    return word_counts


# 示例用法
directory = '../diary'  # 替换为你的日记目录路径
file_format = '.txt'  # 替换为你的日记文件格式
most_common_words = count_most_common_words(directory, file_format)
for i, word_count in enumerate(most_common_words):
    most_common = word_count.most_common(1)
    print(f"在日记文件{i + 1}中，最常出现的单词是：{most_common[0][0]}，出现次数：{most_common[0][1]}次")