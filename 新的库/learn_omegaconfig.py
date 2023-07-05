#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/5 15:44
# @Author   : FengYun
# @File     : learn_omegaconfig.py
# @Software : PyCharm
from omegaconf import OmegaConf

# 从Empty创建OmegaConf
# conf = OmegaConf.create()
# 通过YAML创建OmegaConf
cfg = OmegaConf.create({"foo": {"bar": 12}})
OmegaConf.save(cfg, "test.yaml")
# 读取yaml
conf = OmegaConf.load('config/example.yaml')
cfd = conf.default.lesson
print(cfd)

