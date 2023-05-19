#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/20 09:18
# @Author   : FengYun
# @File     : get_noval.py
# @Software : PyCharm
import requests
import parsel

url = "https://www.douban.com/group/topic/19303114/?_i=1953431DrV9ZVb"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/111.0.0.0 Safari/537.36",
           "Cookie": "bid=DrV9ZVbSWmM; douban-fav-remind=1; __yadk_uid=5DCFgXy83XVtbVRJaSx6Fm2X5DU8IiC7; "
                     "__utmz=30149280.1681261696.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; "
                     "_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1681953435%2C%22https%3A%2F%2Fwww.baidu.com%2Flink"
                     "%3Furl%3D86yPF9YXG2cxoEWYDru8y8r6NSR7zc8J93K44ckW_YSdaO6i1A3LYyv619RUNU87tkL8kTtNyf7PM8WKjgsL7q%26wd%3D%26eqid%3Dbffee72800017098000000066436047a%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __gpi=UID=00000bf26be380c7:T=1681182261:RT=1681953440:S=ALNI_MbEPFV4cBY7TSa8lsOsUAlH06Es2g; __gads=ID=0e6d65eed18ede7a-22a897e927dd00d8:T=1681182261:S=ALNI_MZgXZO36--RSWO4aCa0JuFlvboRPQ; __utma=30149280.1037081700.1681182262.1681261696.1681953444.3; __utmc=30149280; __utmt=1; _pk_id.100001.8cb4=5865f3570eb67770.1681182260.1.1681953611.undefined.; trc_cookie_storage=taboola%2520global%253Auser-id%3D1abacb8e-bf08-401c-91bf-46b14ffccbdc-tuctb3a18cd; __utmb=30149280.6.8.1681953615305"
           }
response = requests.get(url=url, headers=headers)
if response.status_code==200:
    selector = parsel.Selector(response.text)
    result = selector.xpath('//*[@id="link-report"]/div[1]/div/p/text()').get()
    if result is not None:
        with open('data.txt', mode='w', encoding='utf-8') as f :
            f.writelines(result)
        with open('data.txt', mode='r', encoding='utf-8') as input_f :
            lines = input_f.readlines()
        filter_lines = [line.replace('\n', '') for line in lines if line.strip()]
        with open('data.txt', mode='w', encoding='utf-8') as out_f:
            out_f.writelines(filter_lines[1:])
response.close()
