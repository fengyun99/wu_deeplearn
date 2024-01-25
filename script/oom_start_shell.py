#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/24 10:26
# @Author   : FengYun
# @File     : oom_start_shell.py
# @Software : PyCharm
import psutil
import subprocess


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    print(memory_percent)
    if memory_percent > 90:
        subprocess.call(['./a.sh'])


check_memory_usage()
