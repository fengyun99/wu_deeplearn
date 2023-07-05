#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/29 11:01
# @Author   : FengYun
# @File     : test_assist_human.py
# @Software : PyCharm
import json

with open("data/example01.txt", "r", encoding="utf-8") as f:
    for key, row in enumerate(f):
        data = json.loads(row)
        print("data: " + str(data))
        prompt = data["instruction"].strip()
        print("prompt: " + prompt)
        response = data["output"].strip()
        print("response: " + response)
        assist_idx = prompt.rfind("Assistant:")
        print("assist: " + str(assist_idx))
        human_idx = prompt.rfind("Human:")
        print("human: " + str(human_idx))
        query = prompt[human_idx + 6:assist_idx].strip()
        print("query: " + query)
        prompt = prompt[:human_idx].strip()
        print("prompt: " + prompt)
        history = []
        while prompt.rfind("Assistant:") != -1:
            assist_idx = prompt.rfind("Assistant:")
            human_idx = prompt.rfind("Human:")
            if human_idx != -1:
                old_query = prompt[human_idx + 6:assist_idx].strip()
                old_resp = prompt[assist_idx + 10:].strip()
                history.insert(0, (old_query, old_resp))
            else:
                break
            # 把问题后面全部切除
            prompt = prompt[:human_idx].strip()
        print(history)
