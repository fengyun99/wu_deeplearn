#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/25 15:41
# @Author   : FengYun
# @File     : 爬虫.py
# @Software : PyCharm
# 神经网络
import requests
import time

from bs4 import BeautifulSoup
from tqdm import tqdm

fid = 735  # 目标板块的ID
titles735 = []  # 存放爬取的数据
for pid in tqdm(range(1, 80)):
    r = requests.get('https://www.XXX.com/forumdisplay.php?fid=%d&page=%d' % (fid, pid))
    with open('raw_data/%d-%d.html' % (fid, pid), 'wb') as f:  # 原始 HTML 写入文件
        f.write(r.content)
    b = BeautifulSoup(r.text)
    table = b.find('table', id='forum_%d' % fid)  # 寻找返回的HTML中的table 标签
    trs = table.find_all('tr')
    for tr in trs[1:]:
        title = tr.find_all('a')[1].text  # 获取 a 标签中的文字
        titles735.append(title)
    time.sleep(1)  # 阻塞一秒，防止过快的请求给网站服务器造成压力
with open('%d.txt' % fid, 'w', encoding='utf8') as f:  # 把数据写入文件
    for l in titles735:
        f.write(l + '\n')
fid = 644
titles644 = []
for pid in tqdm(range(1, 80)):
    r = requests.get('https://www.XXX.com/forumdisplay.php?fid=%d&page=%d' % (fid, pid))
    with open('raw_data/%d-%d.html' % (fid, pid), 'wb') as f:  # 原始HTML写入文件
        f.write(r.content)
    b = BeautifulSoup(r.text)
    table = b.find('table', id='forum_%d' % fid)
    trs = table.find_all('tr')
    for tr in trs[1:]:
        title = tr.find_all('a')[1].text
        titles644.append(title)
    time.sleep(1)
with open('%d.txt' % fid, 'w', encoding='utf8') as f:
    for l in titles644:
        f.write(l + '\n')
