#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/4 21:02
# @Author   : FengYun
# @File     : test01.py
# @Software : PyCharm
import re

text = "  RT @Aminla #Test\nTom's newly listed Co  &amp; Mary's unlisted   Group to supply tech for n1TK/\nh $TSLA $AAPL http:// t.co/x34afs"

clean_text = re.sub(r'#\w*', ' ', text)

print(clean_text)