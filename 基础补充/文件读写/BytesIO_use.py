#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 20:56
# @Author   : FengYun
# @File     : BytesIO_use.py
# @Software : PyCharm
# 写二进制
# BytesIO写入
from io import BytesIO

f = BytesIO()
f.write('我喜欢学python'.encode('utf-8'))
print(f.getvalue())
# 读取
f = BytesIO(b'\xe6\x88\x91\xe5\x96\x9c\xe6\xac\xa2\xe5\xad\xa6\xe4\xb9\xa0python')
print(f.read().decode('utf-8'))
