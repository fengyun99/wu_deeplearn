#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/18 15:30
# @Author   : FengYun
# @File     : 练习4.py
# @Software : PyCharm
'''
英文纯文本统计词数
'''
with open("data/noval.txt", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace(",", "").replace(".", "").replace("‘", "").replace("?", "").replace(";", "").replace("’",
                                                                                                               "").replace(
    "”", "").replace("“", "").replace("\n\n"," ").replace("\n","").replace("!","")
content_list = content.split(" ")
statistics_word = {}
count = 1
for k in content_list:
    k = k.casefold()
    if k not in statistics_word:
        statistics_word[k] = count
    else:
        statistics_word[k] += 1
print(sorted(statistics_word.items(), key=lambda x:x[1],reverse=True))
