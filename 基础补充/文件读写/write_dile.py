#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 20:37
# @Author   : FengYun
# @File     : write_dile.py
# @Software : PyCharm
import os

list = ['java\n', 'c\n', 'c++\n', 'python\n', 'javascript\n']
try:
    f = open('testWrite3.txt', 'w+')
    f.writelines(list)
    # 将文件指针移动到文件开始位置,移动到0后续读取，写完指针再最后。写完后读！
    f.seek(0)
    # 读取文件内容
    list = f.readlines()
    for line in list:
        print(line.strip())  # 将末尾的'\n'删掉
finally:
    f.close()
