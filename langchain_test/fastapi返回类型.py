#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/28 15:36
# @Author   : FengYun
# @File     : fastapi返回类型.py
# @Software : PyCharm
import time

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import StreamingResponse

app = FastAPI()


@app.get("/items/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


async def fake_video_streamer():
    for i in range(100):
        yield b"some fake video bytes\n"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())

if __name__ == '__main__':
    uvicorn.run("fastapi返回类型:app")
