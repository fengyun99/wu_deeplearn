#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/29 11:22
# @Author   : FengYun
# @File     : 文本切割.py
# @Software : PyCharm
from typing import List
import re


def split_text1(text: str) -> List[str]:
    text = re.sub(r"\n{3,}", "\n", text)
    text = re.sub('\s', ' ', text)
    text = text.replace("\n\n", "")
    sent_sep_pattern = re.compile('([﹒﹔﹖﹗．。！？]["’”」』]{0,2}|(?=["‘“「『]{1,2}|$))')  # del ：；
    sent_list = []
    for ele in sent_sep_pattern.split(text):
        if sent_sep_pattern.match(ele) and sent_list:
            sent_list[-1] += ele
        elif ele:
            sent_list.append(ele)
    return sent_list

a = split_text1('\u3000\u3000住房公积金管理中心应当建立职工住房公积金明细账，记载职工个人住房公积金的缴存、提取等情况。\n\u3000\u3000第十四条\u3000新设立的单位应当自设立之日起30'
            '日内向住房公积金管理中心办理住房公积金缴存登记，并自登记之日起20日内，为本单位职工办理住房公积金账户设立手续。\n\u3000\u3000单位合并、分立、撤销、解散或者破产的，应当自发生上述情况之日起30'
            '日内由原单位或者清算组织向住房公积金管理中心办理变更登记或者注销登记，并自办妥变更登记或者注销登记之日起20日内，为本单位职工办理住房公积金账户转移或者封存手续。\n\u3000\u3000'
            '第十五条\u3000单位录用职工的，应当自录用之日起30日内向住房公积金管理中心办理缴存登记，并办理职工住房公积金账户的设立或者转移手续。\n\u3000\u3000'
            '单位与职工终止劳动关系的，单位应当自劳动关系终止之日起30日内向住房公积金管理中心办理变更登记，并办理职工住房公积金账户转移或者封存手续。\n\u3000\u3000第十六条\u3000'
            '职工住房公积金的月缴存额为职工本人上一年度月平均工资乘以职工住房公积金缴存比例。\n\u3000\u3000单位为职工缴存的住房公积金的月缴存额为职工本人上一年度月平均工资乘以单位住房公积金缴存比例。\n'
            '\u3000\u3000第十七条\u3000新参加工作的职工从参加工作的第二个月开始缴存住房公积金，月缴存额为职工本人当月工资乘以职工住房公积金缴存比例。')

print(a)