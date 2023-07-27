#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/27 14:06
# @Author   : FengYun
# @File     : load_config_code.py
# @Software : PyCharm
import os.path

import yaml
from cryptography.fernet import Fernet


# 生成密钥
def generate_key(filename):
    filename = os.path.basename(filename)
    key = Fernet.generate_key()
    with open(fr"G:\project_key\{filename}.key", "wb") as k:
        k.write(key)


# 加载key
def load_key(filename):
    filename = os.path.basename(filename)
    with open(fr"G:\project_key\{filename}.key", "rb") as k:
        key = k.read()
    return key


# 加密配置文件
def encode_config_file(filename, key):
    with open(filename) as f:
        content = yaml.safe_load(f)
    encode_f = Fernet(key).encrypt(bytes(str(content).encode('utf-8')))
    # 保存二进制文件
    filename = os.path.basename(filename)
    with open(f'config/{filename}.encode', 'wb') as encodef:
        encodef.write(encode_f)


# 解密配置文件
def decode_config_file(filename, key):
    filename = os.path.basename(filename)
    with open(f'config/{filename}.encode', 'rb') as decodef:
        content = decodef.read()
    return Fernet(key).decrypt(content).decode("utf-8")


if __name__ == '__main__':
    FILE_NAME = r"G:\project_config\web_sql.yaml"
    generate_key(FILE_NAME)
    key = load_key(FILE_NAME)
    encode_config_file(FILE_NAME, key)
    print(decode_config_file(FILE_NAME, key))
