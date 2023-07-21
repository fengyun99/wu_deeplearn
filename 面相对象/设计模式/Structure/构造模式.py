#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 13:58
# @Author   : FengYun
# @File     : 构造模式.py
# @Software : PyCharm
from Entity.Hero import Hero
'''
用于控制复杂对象的构造
创建和表示分离。比如你要买电脑，工厂模式直接给你需要的电脑，但是构造模式允许你自己定义电脑的配置，组装完成后给你。
'''


class HeroBuilder:
    def __init__(self):
        self.hero = Hero("Monki")

    def configure_blood(self, amount):
        self.hero.blood = amount

    def configure_attack(self, amount):
        self.hero.attack = amount

    def configure_job(self, job):
        self.hero.job = job


class Game:
    def __init__(self):
        self.builder = None

    def construct_hero(self, blood, attack, job):
        self.builder = HeroBuilder()
        self.builder.configure_blood(blood)
        self.builder.configure_attack(attack),
        self.builder.configure_job(job)

    @property
    def hero(self):
        return self.builder.hero


game = Game()
game.construct_hero(5000, 200, "warrior")
hero = game.hero
print(hero)
