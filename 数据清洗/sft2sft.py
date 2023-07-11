#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/10 15:46
# @Author   : FengYun
# @File     : sft2sft.py
# @Software : PyCharm
import json

with open("精调/change_1.json", "r", encoding="utf-8") as f:
    json_data = f.read()
JSON = json.loads(json_data)
new_json_list = []
for num_json in JSON:
    new_json = {"instruction": "根据天用唯勤员工手册回答下列问题，不在手册中的内容回答“手册内不存在当前内容”", "input": num_json["instruction"], "output": num_json["output"]}
    new_json_list.append(new_json)
json_data = ''
with open("out.json", "w", encoding="utf-8") as f:
    json_data += json.dumps(new_json_list, ensure_ascii=False, indent=2)
    f.write(json_data)