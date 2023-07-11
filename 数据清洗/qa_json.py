#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/10 10:45
# @Author   : FengYun
# @File     : qa_json.py
# @Software : PyCharm
import json
with open("data/Q_data.txt", "r", encoding="utf-8") as f:
    Q = f.read().replace("？","").split("\n")
with open("new.json", "r", encoding="utf-8") as j:
    json_data = j.read()
JSON = json.loads(json_data)
A = "如果员工自认为自己在试用期表现突出可以申请提前转正，提前转正需填写《员工转正申请表》，转正程序与自然转正程序相同。试用期直属领导有权否决提前转正申请。\n如果试用期直属领导对试用员工表现非常认可，在征得部门经理同意后，可以建议员工申请提前转正。"
for i in Q:
    JSON.append({"instruction": f"{i}", "input": "", "output": f"{A}"})
with open("new.json", "w", encoding="utf-8") as outf:
    data_set = json.dumps(JSON, ensure_ascii=False, indent=2) # ensure_ascii取消保存为unicode,indent设置缩进
    outf.write(data_set)
print("json数据传入完成")