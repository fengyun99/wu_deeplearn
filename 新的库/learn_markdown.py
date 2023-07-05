#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/3 14:42
# @Author   : FengYun
# @File     : learn_markdown.py
# @Software : PyCharm
import markdown
html = markdown.markdown("# 1. Hello World")
with open("md.html", "w", encoding="utf-8") as f:
    f.write(html)