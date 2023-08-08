#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/31 15:26
# @Author   : FengYun
# @File     : 08.py
# @Software : PyCharm
'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os


def get_code_lines(directory, file_format):
    code_count = 0
    blank_count = 0
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(file_format):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    if line == '\n':
                        blank_count += 1
                    else:
                        code_count += 1

        return "blank " + str(blank_count) + " code " + str(code_count)


if __name__ == '__main__':
    print(get_code_lines('../06', '.py'))
