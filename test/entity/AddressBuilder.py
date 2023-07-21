#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 15:03
# @Author   : FengYun
# @File     : AddressBuilder.py
# @Software : PyCharm
from Info.Address import Address


class AddressBuilder:
    def __init__(self):
        self._address = Address()

    def conf_address(self, zone: str, building: str, house_number: int):
        self._address.zone = zone
        self._address.building = building
        self._address.house_number = house_number
