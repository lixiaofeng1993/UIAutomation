#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 14:18
# @Author  : lixiaofeng
# @Site    : 
# @File    : page_car_follow.py
# @Software: PyCharm

from common.basics import Crazy


class CarFollowPage(Crazy):
    """元素定位，登录功能"""

    # 点击 关注 or 精选 栏 com.ss.android.auto:id/a1k
    follow_loc = ('xpath', "//*[@class='android.widget.TextView' and @index=0]")

    def click_follow(self):
        self.click(self.follow_loc)

    def text_follow(self):
        return self.get_text(self.follow_loc)

    # 关注人数
    follow_people_num_loc = ('id', 'com.ss.android.auto:id/avr')

    def locator_follow_people_num(self):
        return self.is_locator(self.follow_people_num_loc)

    def text_follow_people_num(self):
        return self.get_text(self.follow_people_num_loc)

    # 选择视频标题
    video_title_loc = ('id', 'com.ss.android.auto:id/c1j')

    def elements_video_title(self):
        return self.find_elements(self.video_title_loc)

    def click_video_title(self, n):
        self.clicks(self.video_title_loc, n)

    def text_video_title(self, n):
        return self.get_texts(self.video_title_loc, n)