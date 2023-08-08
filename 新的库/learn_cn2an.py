#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/1 14:02
# @Author   : FengYun
# @File     : learn_cn2an.py
# @Software : PyCharm
import cn2an
output = cn2an.an2cn('123','low')
print(output)
output = cn2an.an2cn('1234','up')
print(output)
output = cn2an.an2cn('4000000', 'rmb')
print(output)