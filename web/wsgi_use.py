#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.serving import run_simple


def func(environ, start_response):
    print('a')
    pass


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, func)
