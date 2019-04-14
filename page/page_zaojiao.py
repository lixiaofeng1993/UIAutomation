#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 14:31
# @Author  : lixiaofeng
# @File    : page_zaojiao.py
# @Software: PyCharm
# @desc    :

from common.basics import Crazy


class Zaojiaopage(Crazy):
    """视频管理"""

    zao_loc = ('id', 'com.tencent.mm:id/cw')

    def click_zao(self):
        self.click(self.zao_loc)

    def element_zao(self):
        return self.find_element(self.zao_loc)

    find_loc = ('id', 'com.tencent.mm:id/d7b')

    def clicks_find(self):
        self.clicks(self.find_loc, 2)

    small_btn_loc = ('id', 'com.tencent.mm:id/d7v')

    def clicks_small(self):
        self.clicks(self.small_btn_loc, 1)

    # "//*[@class='android.widget.TextView' and @index=0]"
    helper_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="小程序助手"]')

    def click_helper(self):
        self.click(self.helper_loc)

    zaojiao_small_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/c5" and @text="小小包早教"]')

    def element_zaojiao_small_btn(self):
        return self.find_element(self.zaojiao_small_btn_loc)

    delete_small_btn_loc = ('xpath', '//*[contains(@text, "删除")]')

    def click_delete_small_btn(self):
        self.click(self.delete_small_btn_loc)

    edition_btn_loc = ('xpath', '//*[contains(@text, "百宝福利Buy")]')

    def element_edition_btn(self):
        return self.find_element(self.edition_btn_loc)

    version_btn_loc = ('xpath', '//*[contains(@text, "1.1.472")]')

    def click_version_btn(self):
        self.click(self.version_btn_loc)

    delete_small1_btn_loc = ('xpath', '//*[contains(@text, "拖动到此处删除")]')

    def element_delete_small1_btn(self):
        return self.find_element(self.delete_small1_btn_loc)