#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/31 14:38
# @Author   : FengYun
# @File     : 练习.py
# @Software : PyCharm
'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''
import random
import string

import redis

# 创建Redis连接
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def gen_code():
    Str = string.ascii_letters + string.digits
    Promo_Code = []
    Length = 7
    for _ in range(Length):
        Promo_Code.append(random.choice(Str))
    return ''.join(Promo_Code)


# 设置数据
def set_code(code_list: list):
    count = 0
    for code in code_list:
        r.set(count, code)
        count += 1


# 从Redis中读取商品库存数据
def get_code(id):
    code = r.get(id)
    if code is not None:
        return code
    else:
        return None


# 更新商品库存数据到Redis
def update_code(id, code):
    r.set(id, code)


if __name__ == '__main__':
    # code_list = [gen_code() for _ in range(200)]
    # set_code(code_list)
    print(get_code(0))
