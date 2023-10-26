#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/17 15:51
# @Author   : FengYun
# @File     : read_json.py
# @Software : PyCharm
import json

with open('data/hello.json', 'r', encoding='utf-8') as f:
    content = json.load(f)
    print(type(content))