#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/20 11:15
# @Author   : FengYun
# @File     : 模糊搜索.py
# @Software : PyCharm
import ast
import 文本操作.fuzzySearch
import importlib
import pandas as pd

importlib.reload(文本操作.fuzzySearch)
from 文本操作.fuzzySearch import FuzzySearch
fuzzy_search_data_path = "data.csv"
stop_words_path = "stop_word.txt"

fuzzy_search_data = pd.read_csv(fuzzy_search_data_path, header=0)
fuzzy_search_data["embed"] = fuzzy_search_data["embed"].apply(lambda x: ast.literal_eval(x))
fuzzy_search = FuzzySearch(fuzzy_search_data, stop_words_path = stop_words_path)
fuzzy_search.search()
