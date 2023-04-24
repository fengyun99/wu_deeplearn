#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/24 10:30
# @Author   : FengYun
# @File     : excel2json.py
# @Software : PyCharm
import pandas as pd
import json

# 将excel的问答文件转换为json模式
class Excel2JSON:
    def __init__(self, in_filepath: str, out_filename: str):
        self.in_filepath=in_filepath
        self.out_filename=out_filename

    def to_json(self):
        # 读取excel文件
        df = pd.read_excel(self.in_filepath)

        # 将 DataFrame 转换为 JSON 字符串
        json_str = df.to_json(orient='records')

        # 将 JSON 字符串转换为 Python 字典
        data = json.loads(json_str)

        # 添加key对象来声明列表
        json_data = {'handbook': data}

        # 将 Python 字典写入 JSON 文件
        with open(self.out_filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
            print('转换完成')