#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/25 16:17
# @Author   : FengYun
# @File     : 读取html.py
# @Software : PyCharm
import time

from bs4 import BeautifulSoup
from tqdm import tqdm

fid = 735
titles735 = []
for pid in tqdm(range(1, 80)):
    with open(' raw_data /%d-%d.html' % (fid, pid), 'r', encoding='utf8') as f:  # 需选择正确编码
        b = BeautifulSoup(f.read())
    table = b.find('table', id='forum_%d' % fid)
    trs = table.find_all('tr')
    for tr in trs[1:]:
        title = tr.find_all('a')[1].text
        titles735.append(title)
with open('%d.txt' % fid, 'w', encoding='utf8') as f:
    for l in titles735:
        f.write(l + '\n')

fid = 644
titles644 = []
for pid in tqdm(range(1, 80)):
    with open('raw_data/%d-%d.html' % (fid, pid), 'r', encoding='utf8') as f:
        b = BeautifulSoup(f.read())
    b = BeautifulSoup(r.text)
    table = b.find('table', id='forum_%d' % fid)
    trs = table.find_all('tr')
    for tr in trs[1:]:
        title = tr.find_all('a')[1].text
        titles644.append(title)
with open('%d.txt' % fid, 'w', encoding='utf8') as f:
    for l in titles644:
        f.write(l + '\n')
