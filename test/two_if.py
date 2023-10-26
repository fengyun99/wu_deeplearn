#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/14 09:24
# @Author   : FengYun
# @File     : two_if.py
# @Software : PyCharm
sentence = 'abdfg'
if len(sentence) > 0:
    if 'a' in sentence and 'c' not in sentence:
        if 'abd' not in sentence:
            print('yep')
else:
    print('ah')