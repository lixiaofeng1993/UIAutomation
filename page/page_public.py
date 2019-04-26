#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 11:43
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_public.py
# @Software: PyCharm

from common.basics import Crazy


class Pulicpage(Crazy):
    """公众号"""

    choice_public_loc = ('id', 'com.tencent.mm:id/b5m')  # 置顶公众号，默认选择第一个

    def clicks_choice_public(self):
        self.clicks(self.choice_public_loc, 0)

    find_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/d7b" and @text="发现"]')  # 发现按钮

    def click_find(self):
        self.click(self.find_loc)

    search_btn_loc = ('xpath', '//*[@resource-id="android:id/title" and @text="搜一搜"]')  # 搜一搜

    def click_search_btn(self):
        self.click(self.search_btn_loc)

    search_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/kh" and @text="搜索"]')  # 搜索

    def click_search(self):
        self.click(self.search_loc)

    small_zao_loc = ('xpath', '//*[contains(@text, "小小包早教")]')

    def click_small_zao(self):
        self.click(self.small_zao_loc)

    two_small_zao_loc = ('xpath', '//*[contains(@text, "提供原创的母婴类文章，母婴用品评测。")]')  # 搜索后的列表

    def click_two_small_zao(self):
        self.click(self.two_small_zao_loc)

    follow_public_loc = ('xpath', '//*[@resource-id="android:id/title" and @text="关注公众号"]')  # 搜索

    def click_follow_public(self):
        self.click(self.follow_public_loc)

    in_home_zao_btn_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/amt" and @text="在家早教课"]')  # 公众号

    def click_in_home_zao(self):
        self.click(self.in_home_zao_btn_loc)

    qr_code_loc = ('xpath',
                   '//com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View')  # 要识别的二维码

    def element_qr_code(self):
        return self.find_element(self.qr_code_loc)

    discern_code_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/cw" and @text="识别图中二维码"]')  # 识别图中二维码

    def click_discern_code(self):
        self.click(self.discern_code_loc)

    class_group_loc = ('id', 'android:id/text1')  # 群名称

    def text_class_group(self):
        return self.get_text(self.class_group_loc)

    small_zao_title_loc = ('id', 'com.tencent.mm:id/k3')  # 小小包早教公众名称

    def text_small_zao_title(self):
        return self.get_text(self.small_zao_title_loc)

    more_btn_loc = ('id', 'com.tencent.mm:id/jy')  # 三个点

    def click_more_btn(self):
        self.click(self.more_btn_loc)

    not_paying_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/b11" and @text="不再关注"]')  # 不再关注

    def click_not_paying(self):
        self.click(self.not_paying_loc)

    sure_not_paying_loc = ('xpath', '//*[@resource-id="com.tencent.mm:id/az_" and @text="不再关注"]')  # 确定不再关注

    def click_sure_not_paying(self):
        self.click(self.sure_not_paying_loc)

    back_btn_loc = ('id', 'com.tencent.mm:id/kb')  # x 号

    def click_back_btn(self):
        self.click(self.back_btn_loc)
