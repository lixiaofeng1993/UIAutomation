#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 14:18
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_car_follow.py
# @Software: PyCharm

import random
import time
import unittest

from BeautifulReport import BeautifulReport
from page.page_car_follow import CarFollowPage

from common.basics import open_app
from common.logger import Log, img_path
from tmp.eg.page_car_login import CarLoginPage


class TestCarLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.car = CarLoginPage(cls.driver)
        cls.follow = CarFollowPage(cls.driver)
        cls.tag_name = ''
        # cls.img_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'report\img')
        cls.img_path = img_path  # 必须是这个路径

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('follow')
    def test_tag(self):
        car = self.car
        follow = self.follow
        try:
            car.click_skip()  # 跳过广告
        except AttributeError as e:
            pass
        self.assertEqual(car.text_landed(), '我的', '未检测到用户登录，无法进行相关操作！')
        follow.click_follow()
        self.tag_name = follow.text_follow()
        self.log.info('用户为登录状态，准备进行 {} 操作.'.format(self.tag_name))
        self.save_img('follow')

    def text_follow(self):
        follow = self.follow
        if self.tag_name == '关注':
            if follow.locator_follow_people_num():
                self.log.info('当前用户未关注任何人，准备进行关注别人操作.')
            else:
                self.log.info('当前用户已关注他人，准备进行浏览操作.')
        elif self.tag_name == '精选':
            follow.swipeDown()
            video_num = len(follow.elements_video_title())
            ran = random.random(0, video_num)
            print(ran)
            follow.click_video_title(ran)
            self.log.info('选择 {} 条目查看.'.format(follow.text_video_title(ran)))

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
