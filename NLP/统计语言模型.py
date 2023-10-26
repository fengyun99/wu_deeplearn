#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 16:30
# @Author   : FengYun
# @File     : 统计语言模型.py
# @Software : PyCharm

from collections import Counter

corpus = '''她的菜很好 她的菜很香 她的他很好 他的菜很香 他的她很好 
很香的菜 很好的她 很菜的他 她的好 菜的香 他的菜 她很好 他很菜 菜很好'''.split()
# 统计词频
counter = Counter()
for sentence in corpus:
    for word in sentence:
        counter[word] += 1
counter = counter.most_common()
lens = len(counter)
word2id = {counter[i][0]: i for i in range(lens)}
id2word = {i: w for w, i in word2id.items()}
# 构建字典
print(word2id)
print(id2word)


