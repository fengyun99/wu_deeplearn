#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/30 09:40
# @Author   : FengYun
# @File     : 流式请求本地api.py
# @Software : PyCharm
import json

import requests


def stream():
    url = "http://192.168.2.103:8001/v1/chat/completions"
    data = {
        "model": "baichuan13b",
        "messages": [{"role": "user", "content": "你好"}],
        "temperature": 0.1,
        "stream": "True"
    }
    response = requests.post(url=url, data=json.dumps(data)).text
    for trunk in response:
        print(trunk)
        # if trunk['choices'][0]['finish_reason'] is not None:
        #     data = '[DONE]'
        # else:
        #     data = trunk['choices'][0]['delta'].get('content', '')
        # print(data)
    #     yield "data: %s\n\n" % data.replace("\n", "<br>")
    # return flask.Response(stream(), mimetype="text/event-stream")


if __name__ == '__main__':
    stream()
