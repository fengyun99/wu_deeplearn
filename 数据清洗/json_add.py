#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 10:01
# @Author   : FengYun
# @File     : json_add.py
# @Software : PyCharm
import json
import ast
with open("add/alpaca_gpt4_data_zh.json", "r", encoding="utf-8") as f1:
    content1 = f1.read()
json1 = json.loads(content1)
with open("精调/change_1.json", "r", encoding="utf-8") as f2:
    content2 = f2.read()
json2 = json.loads(content2)
out_json = list(json1)+list(json2)
print(out_json[-1])
# with open("merge.json", "w", encoding="utf-8") as merge:
#     out = json.dumps(out_json, ensure_ascii=False, indent=2)
#     content = merge.write(out)
