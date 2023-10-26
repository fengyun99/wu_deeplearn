#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 21:23
# @Author   : FengYun
# @File     : 可变字符串.py
# @Software : PyCharm
import io

s = "hello,bjsxt"
sio = io.StringIO(s)
print(sio)
print('原字符串：', sio.getvalue())
sio.seek(7)  # index 7
sio.write("g")
print('修改后字符串：', sio.getvalue())
